import pytorch_lightning as pl
import pandas as pd
import torch
import transformers
from sklearn.model_selection import KFold


class Dataloader(pl.LightningDataModule):
    def __init__(self, model_name, batch_size, shuffle,
                 train_path, dev_path, test_path, predict_path,
                 k_fold=True, num_split=10, k=1, seed=11,):
        super().__init__()
        # Base Info
        self.model_name = model_name
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.seed = seed

        # Path
        self.train_path = train_path
        self.dev_path = dev_path
        self.test_path = test_path
        self.predict_path = predict_path

        # Dataset Init
        self.train_dataset = None
        self.val_dataset = None
        self.test_dataset = None
        self.predict_dataset = None

        # Preproces
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(
            model_name, max_length=160)
        self.target_columns = ['label']
        self.delete_columns = ['id']
        self.text_columns = ['sentence_1', 'sentence_2']

        self.automatic_optimization = False

        # K-Fold
        self.k_fold = k_fold
        self.num_split = num_split
        self.k = k

    # 추가 정의 함수 구간.
    # def aug_switched_sentence(self, df, switched_columns, frac_v=0.8):
    # def aug_rand_del(self, df, p=0.2):
    # def aug_rand_swap(self, df, p=0.2):
    # def aug_only_middle(self, df, p=0.2):
    # def prepro_spell_checker(self, data):
    # def tokenizing(self, df_input):
    # def preprocessing(self, data):


    def setup(self, stage='fit'):
        if stage == 'fit':
            # 학습 데이터와 검증 데이터셋을 호출합니다
            train_data = pd.read_csv(self.train_path)
            val_data = pd.read_csv(self.dev_path)

            # 학습데이터 준비
            # train_data = self.aug_switched_sentence(
            #     train_data, switched_columns=self.text_columns) 
            # train_data = self.aug_rand_del(train_data) 
            # train_data = self.aug_rand_swap(train_data) 
            # train_data = self.aug_only_middle(train_data) 
            # 다양한 data aug는 여기에서
            self.after_aug_train_data = train_data

            # 검증데이터 준비
            val_data = self.prepro_spell_checker(val_data)
            if self.k_fold:
                total_data = pd.concat([train_data, val_data], axis=0)
                total_input, total_targets = self.preprocessing(total_data)
                total_dataset = Dataset(total_input, total_targets)

                kf = KFold(n_splits=self.num_split, shuffle=True, random_state=self.seed)
                all_splits = [k for k in kf.split(total_dataset)]

                train_idx, val_idx = all_splits[self.k]
                train_idx, val_idx = train_idx.tolist(), val_idx.tolist()

                self.train_dataset = [total_dataset[i] for i in train_idx]
                self.after_aug_train_data = total_data.iloc[train_idx, :]
                self.val_dataset = [total_dataset[i] for i in val_idx]
            else:
                # 학습데이터 준비
                train_inputs, train_targets = self.preprocessing(train_data)

                # 검증데이터 준비
                val_inputs, val_targets = self.preprocessing(val_data)

                # train 데이터만 shuffle을 적용해줍니다, 필요하다면 val, test 데이터에도 shuffle을 적용할 수 있습니다
                self.train_dataset = Dataset(train_inputs, train_targets)
                self.val_dataset = Dataset(val_inputs, val_targets)
        else:
            # 평가데이터 준비
            test_data = pd.read_csv(self.test_path)
            test_data = self.prepro_spell_checker(test_data)
            test_inputs, test_targets = self.preprocessing(test_data)
            self.test_dataset = Dataset(test_inputs, test_targets)

            predict_data = pd.read_csv(self.predict_path)
            predict_data = self.prepro_spell_checker(predict_data)
            predict_inputs, predict_targets = self.preprocessing(predict_data)
            self.predict_dataset = Dataset(predict_inputs, [])

    def train_dataloader(self):
        # def make_sampler(train_data):

        # shuffle=args.shuffle
        return torch.utils.data.DataLoader(self.train_dataset, batch_size=self.batch_size, num_workers=8, sampler=make_sampler(self.after_aug_train_data))

    def val_dataloader(self):
        return torch.utils.data.DataLoader(self.val_dataset, batch_size=self.batch_size)

    def test_dataloader(self):
        return torch.utils.data.DataLoader(self.test_dataset, batch_size=self.batch_size)

    def predict_dataloader(self):
        return torch.utils.data.DataLoader(self.predict_dataset, batch_size=self.batch_size)

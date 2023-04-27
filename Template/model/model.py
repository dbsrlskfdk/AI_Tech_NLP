"""
model.py
    * KcELECTRA, RoBERTa 등의 모델을 정의한 py file. 
    * 아래와 같은 dict 형태로 모델 생성시 넘겨주면 됩니다. 

    {
        "model_name": "beomi/KcELECTRA-base",

        "fn_loss": nn.CrossEntropyLoss(),

        "learning_rate": 1e-5,

        "fn_optimizer": AdamW(),

        "optimizer_setting": [
        
            {
            
                'scheduler': scheduler,

                'interval': 'step',

                'frequency': 1,

                'reduce_on_plateau': False,

                'monitor': 'val_loss',

            }

        ],

        ...

    }

TODO:
    * Model class 생성. 
    * 이전 파일에서 참고 지점 가져오기. 
    * Model 최대한 추상화 하기. 
"""

import pytorch_lightning as pl
import torchmetrics

from transformers import AutoModelForSequenceClassification


class Model(pl.LightningModule):
    """
    Model
        KcELECTRA, RoBERTa 등의 모델에 사용 가능한 Model class. 
    """

    def __init__(self, config: dict) -> None:
        """
        __init__
            config를 이용한 모델 생성자 함수. 

        Args:
            config (dict): Model에 적용 할 dictionary. 
        """

        super().__init__()

        # 설정 값 객체에 저장.
        self.__config = config

        self.__model_name = config["model_name"]
        self.__loss = config["fn_loss"]
        self.__lr = config["learning_rate"]
        self.__optimizer = config["fn_optimizer"]
        self.__optimizer_setting = config["optimizer_setting"]

        # Pre-trained model 불러오기.
        self.__pre_model = AutoModelForSequenceClassification.from_pretrained(
            pretrained_model_name_or_path=self.__model_name,
            num_labels=1)

    def forward(self, x):
        """
        인자값 x를 이용하여 추론 후 결과 반환. 

        Args:
            x: 모델 추론에 사용 할 input 값. 

        Returns:
            x: 추론된 결과값. 
        """
        x = self.__pre_model(x)['logits']

        return x

    def training_step(self, batch, batch_idx):
        """
        training 시 호출되는 함수.
        batch와 batch_idx를 받아 결과에 대한 loss에 대해 반환.

        Args:
            batch:      Dataloader에서 feed된 batch.
            batch_idx:  Dataloader에서 feed된 batch의 index. (사용되지 않음. )

        Returns:
            loss: batch에서 추론된 값에 대해, 설정된 loss function을 이용하여 계산된 loss.
        """

        x, y = batch

        logits = self(x)
        loss = self.__loss(logits, y.float())
        self.log("train_loss", loss)

        return loss

    def validation_step(self, batch, batch_idx):
        """
        Validation 시 호출되는 함수.
        batch와 batch_idx를 받아 결과에 대한 pearson score를 계산하여 반환. 

        Args:
            batch:      Dataloader에서 feed된 batch.
            batch_idx:  Dataloader에서 feed된 batch의 index. (사용되지 않음. )

        Returns:
            loss: batch에서 추론된 값에 대해, target값에 대한 pearson 상관계수. 
        """

        x, y = batch
        logits = self(x)
        loss = self.__loss(logits, y.float())
        self.log("val_loss", loss)

        self.log("val_pearson", torchmetrics.functional.pearson_corrcoef(
            logits.squeeze(), y.squeeze()))

        return loss

    def test_step(self, batch, batch_idx):
        """
        Test 시 호출되는 함수.
        batch와 batch_idx를 받아 결과에 대한 pearson score를 계산하여 반환. 

        Args:
            batch:      Dataloader에서 feed된 batch.
            batch_idx:  Dataloader에서 feed된 batch의 index. (사용되지 않음. )

        Returns:
            loss: batch에서 추론된 값에 대해, target값에 대한 pearson 상관계수. 
        """

        x, y = batch
        logits = self(x)

        self.log("test_pearson", torchmetrics.functional.pearson_corrcoef(
            logits.squeeze(), y.squeeze()))

    def predict_step(self, batch, batch_idx):
        """
        추론 시 호출되는 함수.
        batch와 batch_idx를 받아 결과에 대한 pearson score를 계산하여 반환. 

        Args:
            batch:      Dataloader에서 feed된 batch.
            batch_idx:  Dataloader에서 feed된 batch의 index. (사용되지 않음. )

        Returns:
            x: 학습 된 모델에서 추론한 결과값. 
        """

        logits = self(batch)

        return logits.squeeze()

    def configure_optimizers(self):
        """
        Optimizer에 대한 설정을 반환하는 함수. 

        Returns:
            Optimizer과 optimizer의 설정값. 
        """

        optimizer = self.__optimizer(self.parameters(), lr=self.__lr)

        return ([optimizer], self.__optimizer_setting)

import argparse
import pytorch_lightning as pl
import pandas as pd
import torch

'''
    main 부분에서 저장한 모델의 파일명과 가중치를 직접 지정합니다.
    저장한 모델의 파일명에 roberta 또는 kcelectra가 포함되어 있다고 가정합니다.
'''

if __name__ == '__main__':
    '''
        model.pt 파일들과 가중치 정보로 앙상블 하여 하나의 output.csv를 만듭니다.
        parser의 predict_path에 있는 csv파일을 예측합니다.
    '''
    # set parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--shuffle', default=False)
    parser.add_argument('--batch_size', default=16, type=int)
    parser.add_argument('--accelerator', default='gpu')
    parser.add_argument('--train_path', default='~/data/train.csv')
    parser.add_argument('--dev_path', default='~/data/dev.csv')
    parser.add_argument('--test_path', default='~/data/dev.csv')
    parser.add_argument('--predict_path', default='~/data/test.csv')
    parser.add_argument('--submission_path', default='~/data/sample_submission.csv')
    args = parser.parse_args()

    # 불러올 모델들의 pt파일과 해당하는 모델의 가중치를 설정합니다.
    models = ['exampleRoberta1.pt', 'exampleRoberta2.pt','exampleRoberta3.pt',
                  'exampleELECTRA1.pt', 'exampleELECTRA2.pt', 'exampleELECTRA3.pt']
    model_weights = [0.3, 0.1, 0.1, 0.2, 0.2, 0.1]

    prediction = []

    for model_path in models:
        #모델을 불러옵니다.
        model = torch.load('./saved/' + model_path)

        # 파일명에 roberta가 있으면 model_name을 klue/roberta-large로 지정합니다
        if 'roberta' in model_path.lower():
            model_name = 'klue/roberta-large'
            # args.batch_size = 16

        # 파일명에 kcelectra가 있으면 model_name을 beomi/KcELECTRA-base-v2022로 지정합니다
        elif 'kcelectra' in model_path.lower():
            model_name = 'beomi/KcELECTRA-base-v2022'
            # args.batch_size = 24
        else:
            raise ValueError("Invalid model name")

        # 기존의 Dataloader를 사용합니다.
        dataloader = Dataloader(model_name, args.batch_size, args.shuffle, args.train_path, args.dev_path,
                                args.test_path, args.predict_path)
        
        # trainer를 설정합니다.
        trainer = pl.Trainer(accelerator=args.accelerator)

        # predict한 뒤 prediction에 append에 추가합니다
        prediction.append(torch.cat(trainer.predict(
            model=model, datamodule=dataloader)))
        
    # 가중치를 적용해 앙상블합니다.
    prediction = torch.stack(prediction).transpose(0, 1)
    weighted_ensemble = torch.sum(model_weights * prediction, dim=0)
    
    # output.csv를 만듭니다.
    output = pd.read_csv(args.submission_path)
    output['target'] = weighted_ensemble
    output['target'] = output['target'].applymap(lambda x: min(max(0.0, x), 5.0))
    output.to_csv('output.csv', index=False)
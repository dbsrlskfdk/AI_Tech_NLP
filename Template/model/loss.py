import torch.nn as nn

'''
    config [loss] 부분의 loss_name 을 바꾸어
    Model 부분의 self.loss_fn = Loss(config)로 사용할 수 있습니다.
'''

class Loss(nn.Module):
    def __init__(self, config):
        super(Loss, self).__init__()
        """
            config로 부터 loss_fn을 설정합니다.
        """
        # config에서 loss 함수 이름을 가져옵니다.
        self.loss_name = config['loss']['loss_name']
        
        # loss 함수를 설정합니다.
        if self.loss_name == 'mse':
            self.loss_fn = nn.MSELoss()
        elif self.loss_name == 'l1':
            self.loss_fn = nn.L1Loss()
        else:
            raise ValueError(f"Unsupported loss function: {self.loss_name}")
        
    def forward(self, inputs, targets):
        """
        loss 값을 계산하는 함수.
        inputs와 targets을 받아 loss_fn으로 loss를 계산하여 반환. 
        Args:
            inputs: 모델이 추론한 예측값.
            targets: 실제값
        Returns:
            loss: loss_fn 계산한 loss값. 
        """
        loss = self.loss_fn(inputs, targets)
        return loss
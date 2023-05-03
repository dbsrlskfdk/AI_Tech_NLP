import torch.optim as optim
'''
    Model 부분에서 self.optimizer = get_optimizer(self.parameters(), config) 으로 optimizer을 선언 후
    configure_optimizers에서 return self.optimizer를 해야합니다.
    만약 스케줄러가 있다면 configure_optimizers에서 return [optimizer], [scheduler] 으로 반환합니다.
    config에서 optimizer_type의 변경으로 AdamW와 AdamP를 선택합니다.
'''
def get_optimizer(model_parameters, config):
    """
        config 로 부터 optimizer_type을 읽어 optimizer를 설정합니다.
        Args:
            model_parameters: 모델의 파라미터 값.
            config: config 객체.
        Returns:
            optimizer: 설정한 optimizer. 
    """
    
    # config에서 optimizer_type과 learning_rate를 가져옵니다.
    optimizer_type = config.optimizer.type
    lr = config.optimizer.learning_rate
    
    # optimizer를 설정합니다.
    if optimizer_type == "AdamP":
        optimizer = optim.AdamP(model_parameters, lr=lr)
    elif optimizer_type == "AdamW":
        optimizer = optim.AdamW(model_parameters, lr=lr)
    else:
        raise ValueError("Invalid optimizer type")

    return optimizer
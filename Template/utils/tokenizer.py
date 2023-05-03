from transformers import AutoTokenizer
'''
    Data 부분에서 self.tokenizer = get_tokenizer(config) 으로 tokenizer를 선언합니다.
    config를 수정하여 model_name 과 max_length를 지정합니다.
'''
def get_tokenizer(config):
    """
        config 로 부터 model_name과 max_length을 읽어 tokenizer를 설정합니다.
        Args:
            config: config 객체.
        Returns:
            tokenizer: 설정한 tokenizer. 
    """
    # config 파일에서 tokenizer 관련 설정을 가져옵니다
    model_name = config.tokenizer.model_name
    max_length = config.tokenizer.max_length

    # tokenizer를 생성합니다.
    tokenizer = AutoTokenizer.from_pretrained(model_name, max_length=max_length)

    return tokenizer
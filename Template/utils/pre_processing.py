import pandas as pd
import configparser
import pathlib
import re
# !pip install emoji
import emoji
from pandas import DataFrame

# !pip install soynlp
from soynlp.normalizer import repeat_normalize
# !pip install git+https://github.com/jungin500/py-hanspell
from hanspell import spell_checker
from typing import List, Tuple, Any

config = configparser.ConfigParser()
config_path = pathlib.Path.cwd().parent / "config.cfg"
config.read(config_path)


# #KcElectra 사용을 위한 Text Preprocessing
def kcelectra_clean(x: str) -> str:
    """
    KcELECTRA를 사용하기 위한 Text Preprocessing
    https://github.com/Beomi/KcELECTRA 참고

    Args:
        x: Pre-Process를 수행할 Text

    Returns:
        KcELECTRA를 위한 전처리가 완료된 Text.
    """

    pattern = re.compile(f'[^ .,?!/@$%~％·∼()\x00-\x7Fㄱ-ㅣ가-힣]+')  # 한글, 영어, 숫자, 특수문자 패턴
    url_pattern = re.compile(
        r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')  # url 패턴

    x = pattern.sub(' ', x)  # 한글, 영어, 숫자, 특수문자 글자를 ' '로 대체
    x = emoji.replace_emoji(x, replace='')  # emoji 삭제
    x = url_pattern.sub('', x)  # url 삭제
    x = x.strip()
    x = repeat_normalize(x, num_repeats=2)  # 여러 글자 중복 케이스, 2개까지로 줄이기
    return x


def aug_switched_sentence(df: pd.DataFrame, switched_columns: List, frac_v: float = 0.8) -> pd.DataFrame:
    """
    switched_columns의 column을 서로 바꾸고, 같은 label을 갖도록 source datframe에 더해주어 반환.
    Args:
        df: 증강 할 source dataframe
        switched_columns: 바꿀 column
        frac_v: 증강시킬 비율

    Returns:
        switched_columns가 바뀌고, 같은 label을 갖도록 증강된 dataframe
    """
    sampled_train_data = df.sample(
        frac=frac_v, random_state=config['SETTINGS'].getfloat('SEED'), replace=False)
    sampled_train_data[switched_columns[0]], sampled_train_data[switched_columns[1]] = \
        sampled_train_data[switched_columns[1]], sampled_train_data[switched_columns[0]]
    df = pd.concat([df, sampled_train_data], axis=0)
    df = df.reset_index(drop=True)
    return df


def spell_check(text_columns: List, data: pd.DataFrame) -> pd.DataFrame:
    """
    text_columns에 해당하는 column의 text를 hanspell을 이용해, spell check하여 반환.
    :param text_columns: spell check할 text column
    :param data: source dataframe
    :return: data에 text_columns의 text가 spell check된 dataframe.
    """
    data[text_columns] = data[text_columns].applymap(
        lambda x: spell_checker.check(re.sub("&", " ", x)).checked)
    return data


def drop_non_use_columns(data: pd.DataFrame, delete_columns: List, target_columns: List = None) -> tuple[
    pd.DataFrame | Any, list[Any] | Any]:
    """
    data에서 delete_columns를 제거하고, target_columns를 반환.
    Args:
        data: source dataframe
        delete_columns: 삭제할 columns
        target_columns: target columns

    Returns:
        data에서 delete_columns를 제거하고, target_columns를 반환.
    """
    data = data.drop(columns=delete_columns)

    try:
        targets = data[target_columns].values.tolist()
    except:
        targets = []

    return data, targets

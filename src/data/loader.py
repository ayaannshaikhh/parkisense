import kagglehub
from kagglehub import KaggleDatasetAdapter


def load_tremor_dataset(file_path="train.csv"):
    df = kagglehub.load_dataset(
        KaggleDatasetAdapter.PANDAS,
        "nikee7/parkinsons-tremor-classification-dataset",
        file_path,
    )
    return df


if __name__ == "__main__":
    df = load_tremor_dataset()
    print(df.head())
# Creating a Virtual Environment
```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```
---
# Trial Run
Use `train.csv` as the file path in `src/data/loader.py`
## Output
```
Downloading to /Users/root/.cache/kagglehub/datasets/nikee7/parkinsons-tremor-classification-dataset/versions/1/train.csv...
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 65.0k/65.0k [00:00<00:00, 67.0MB/s]
                                      data_file_name      folder_path gender  age patient_off_on  doctor_diagnosis_0_5
0  raw_data_d786d645-db38-11ec-b494-e82aea2c97f4.csv   Kinetic tremor   Male   52            off                     1
1  raw_data_bdcba44f-0d6a-11ed-8857-b6da2cf29e9d.csv  Postural tremor   Male   78             on                     0
2  raw_data_750c0f09-b09a-11ec-9699-58a023d3f6d9.csv  Postural tremor   Male   71             on                     0
3  raw_data_d90846c3-3969-11ed-a96d-b469216ca443.csv             Fist   Male   23            off                     1
4  raw_data_c27fbeb3-1882-11ed-95c1-b469216ca443.csv   Kinetic tremor   Male   23            off                     2
```
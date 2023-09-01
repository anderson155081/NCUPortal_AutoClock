# NCUPortal_AutoClock
An automation tool to help clock in / out on NCUPortal.
中央大學自動簽到/退

### 💻 Installation

1. Clone the NCUPortal_AutoClock repository:

```sh
git clone https://github.com/anderson155081/NCUPortal_AutoClock.git && cd NCUPortal_AutoClock
```

2. Create a Conda environment and install selenium:

```sh
conda create --name autoclock python=3.9
conda activate autoclock
pip install -r requirements.txt
```
3. create a file .env:

```env
USERNAME = "Your Student/teacher ID"
PASSWORD = "Your Password"
LINE_NOTIFY_TOKEN = "" 
```
4. edit the json file data.json:

```json
[
    {
        "job_code": "",
        "start_time": "09:00",
        "end_time": "17:05",
        "run_date": "2,6",
        "message": ""
    }
    //add on if you have more than one job
]
```
```

run_date:
    "2-15" = Every month from the 2nd to the 15th.每個月2-15號
    "2" = Every month on the 2nd.每個月2號
    "everyday" = Every day.每天執行

```

5. Run:

```sh
python main.py
```

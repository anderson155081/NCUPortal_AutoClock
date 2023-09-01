# NCUPortal_AutoClock 🕰️  

Automate your clock-in and clock-out activities at Central University with ease!

![Language](https://img.shields.io/badge/python-3.9-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

中央大學自動簽到/退

---



## 💻 Installation & Setup
&nbsp;  

### Step 1: Clone the Repository 📂
```sh
git clone https://github.com/anderson155081/NCUPortal_AutoClock.git && cd NCUPortal_AutoClock
```
&nbsp;  
### Step 2: Create a Virtual Environment(Optional) 🛠️ 
```sh

conda create --name autoclock python=3.9
conda activate autoclock
pip install -r requirements.txt

```
&nbsp;
### Step 3: Configure Environment Variables 🌍
Create a .env file in the root directory.  
If you'd like to receive LINE notifications, acquire your token from [LINE_NOTIFY](https://notify-bot.line.me/zh_TW/) and add it to the .env file.  
    
```env
USERNAME = "Your Student-ID/Account"
PASSWORD = "Your Password"
LINE_NOTIFY_TOKEN = "" 
```
&nbsp;
### Step 4: Edit Data File 🗃️  
Edit the `data.json` file with your job code and preferences.  

> #### Note: Find your job code as shown below:  
> <img width="682" alt="截圖 2023-09-01 下午6 27 44" src="https://github.com/anderson155081/NCUPortal_AutoClock/assets/46291688/0a6fd79e-0a52-487c-a586-cc9778261d7e">

```json

[
    {
        "job_code": "",
        "start_time": "09:00",
        "end_time": "17:05",
        "run_date": "2,6",
        "message": ""
    }
]
```

#### Explanation of `run_date`:  

* "2-15" = Every month from the 2nd to the 15th.每個月2-15號
* "2" = Every month on the 2nd.每個月2號
* "everyday" = Every day.每天執行
  
&nbsp;

### Step 5: Run the Program 🚀
```sh
python main.py
```
&nbsp;
---  
### 📝 License
#### This project is licensed under the MIT License. See the [LICENSE.md]() file for details.
---  

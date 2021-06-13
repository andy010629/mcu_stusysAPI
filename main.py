from fastapi import FastAPI,Response
from pydantic import BaseModel
import requests

app = FastAPI()

class LoginInfo(BaseModel):
    uu: str
    pp: str


@app.post("/api/login")
async def Login(info: LoginInfo,response: Response):
    r =  requests.post('https://www.mcu.edu.tw/student/new-query/Chk_Pass_New_v1.asp?t_tea_no=08360903&t_tea_pass=andy900629')
    url = 'https://www.mcu.edu.tw/student/new-query/Chk_Pass_New_v1.asp'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'
    }
    data = {
        't_tea_no':info.uu,
        't_tea_pass':info.pp,
    }
    login_in = requests.post(url, headers = headers, data = data)
   
    
    loginpass =  'std%5Fenm' in login_in.cookies
    cookies = login_in.cookies
    if not loginpass:
        return 401
    else:
        for ele in cookies:
            response.set_cookie(key=ele.name, value=ele.value)
        return 200
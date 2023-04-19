from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def canChangeFuntionName():
    #async를 앞에 붙임으로써 해당 함수 비동기 처리, 이런 함수를 코루틴 이라 칭함
	return { "message" : "Hello orld123123" }

#uvicorn main:app --reload  명령어로 서버 실행
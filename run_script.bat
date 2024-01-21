@echo off
cd C:\Users\User\PycharmProjects\pythonProject\Malaysia\test
call C:\Users\User\anaconda3\Scripts\activate.bat Malaysia
kedro run --pipeline blood_donation_trend
kedro run --pipeline donator_retention

cd C:\Users\User\PycharmProjects\pythonProject\Malaysia\test
call C:\Users\User\anaconda3\Scripts\activate.bat Malaysia
C:\Users\User\anaconda3\envs\Malaysia\python.exe main.py

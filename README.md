# TaskBot

# V1

- description :
  - bot that sends notification message every hour
    - to user only
- requirements :
  - telebot UI
    - available commands :
      - `add` - add job to scheduler
        - _job_name_
        - _interval_ (set hour/minute/second) (set off-hours)
        - _function_ (list of pre-defined ones?)
      - `stop` - remove job from scheduler
      - `stop-all` - remove all jobs from scheduler
      - `list` - list all running jobs (job_name, function/description)
      - ...
      - `help`
      - `view` - check job logs?
  - apscheduler management
    - JobStore management :
      1. list (job names only)
      2. dict (job names with descriptions)
      3. list/dict of objects
      4. database (redis / sqlite)
    - scheduler APIs :
      - add/remove job(s)
      - ...
      - security?

##Packages (list required packages & run .scripts/python-init.sh)
flask
pandas
pendulum
apscheduler
pyTelegramBotAPI
##Packages

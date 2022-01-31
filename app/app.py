from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask import Flask, request
import json

from utils import getDateTime

scheduler = BackgroundScheduler(timezone='Asia/Singapore')
scheduler.start()

# crontab = CronTrigger.from_crontab('*/1 * * * *')
customJobStore = []

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def _main():
    if request.method == 'GET':
        return 'Documentation Here:\n...', 200
    elif request.method == 'POST':
        # init <class> from data
        data = request.json
        if 'action' in data.keys():
            name = data['name']
            if name not in customJobStore:
                if data['action'] == 'ADD':
                    customJobStore.append(name)
                    scheduler.add_job(getDateTime, trigger='cron', id=name, second='*/5')
                    return f'Job={name} added...', 200
                elif data['action'] == 'STOP':
                    return 'Job not found...', 400
                else:
                    return 'Invalid "action"...', 400
            else:
                if data['action'] == 'ADD':
                    return f'Job={name} is in used...', 400
                if data['action'] == 'STOP':
                    customJobStore.remove(name)
                    scheduler.remove_job(job_id=name)
                    return f'Job={name} removed...', 200
                else:
                    return 'Invalid "action"...', 400
        else:
            return 'Invalid data received', 400
    else:
        return 'Method not supported...', 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)

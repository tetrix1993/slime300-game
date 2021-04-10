import requests
import multiprocessing


# Sends GET/POST Request to increase the global score in https://game.slime300-anime.com/


PUT_REQUEST = 'https://game.slime300-anime.com/put.php'
GET_REQUEST = 'https://game.slime300-anime.com/get.php'
MAX_ITERATIONS = 100  # Set -1 to run forever
PROCESSES = 30  # Number of process to send GET/POST Requests concurrently


def run_process(pid):
    iteration = 0
    while iteration < MAX_ITERATIONS or MAX_ITERATIONS == -1:
        iteration += 1
        try:
            r = requests.get(GET_REQUEST)
            json_obj = r.json()
            token = json_obj['token']
            phpsessid = r.cookies.get_dict()['PHPSESSID']

            form_data = {'token': token,
                         'action': 'BEAT_SLIME',
                         'num': '559'}
            p_response = requests.post(PUT_REQUEST, data=form_data, headers={'cookie': 'PHPSESSID=%s' % phpsessid})
            p_response_obj = p_response.json()
            exp = p_response_obj['exp']

            print(f'Process {pid} - Experience: {exp}')
        except Exception as e:
            pass


def run():
    with multiprocessing.Pool(PROCESSES) as p:
        results = []
        for i in range(PROCESSES):
            result = p.apply_async(run_process, (str(i + 1).zfill(2),))
            results.append(result)
        for result in results:
            result.wait()


if __name__ == '__main__':
    run()

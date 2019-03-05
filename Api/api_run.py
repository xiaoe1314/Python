"""
    Created by 朝南而行 2019/1/21 9:16
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='666', debug=app.config['DEBUG'])

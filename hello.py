from flask import Flask
from is_prime import prime

app = Flask(__name__)


@app.route('/')
def hundred_primes():
    return str(prime(100))


@app.route('/<int:n>', methods=['GET'])
def get_first_n_primes(n):
    return str(prime(n))


if __name__ == '__main__':
    app.run(debug=True)

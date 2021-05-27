test = {   'name': 'q1_3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(y_hat) == len(y)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> x.shape == (30000,)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 0.1 <= beta <= 0.2\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> 23000 <= alpha <= 25000\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.isclose(beta, 0.16199038569776522)\nTrue', 'hidden': True, 'locked': False},
                                   {'code': '>>> np.isclose(alpha, 24092.480872897704)\nTrue', 'hidden': True, 'locked': False},
                                   {   'code': '>>> np.random.seed(1234);\n'
                                               '>>> sub_y = np.random.choice(y_hat, 5);\n'
                                               '>>> np.allclose(sub_y, [48391.03872756, 28952.19244383, 87268.73129503, 58110.46186943, 32192.00015779])\n'
                                               'True',
                                       'hidden': True,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

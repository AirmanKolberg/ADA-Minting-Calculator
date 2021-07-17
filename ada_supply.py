import cryptocompare


def get_ada_supply():

    ada_supply = cryptocompare.get_price(coin='ADA',
                                         currency='USD',
                                         full=True)['RAW']['ADA']['USD']['SUPPLY']
    return ada_supply


if __name__ == '__main__':

    pass
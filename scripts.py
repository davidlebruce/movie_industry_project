def conversion_rates(x):
    '''
       When given a string with the leading 3-letter country code followed by a numerical value,
       return the foreign currencies USD equivelant.

    Parameters
    ----------
    string representing foreign currency with the country abbreviation before the numerical value.


    Returns
    -------

    Float containing the foreign currency converted to USD.


    Examples
    --------

    >>> conversion_rates('AUD160,000,000')
    114832800.00


    '''
    list_of_curr = {'ARS':0.01, 'AUD':0.54, 'BGL':0, 'BRL':0.13, 'CAD':0.55, 'CHF':0.8, 'CLP':0.0009, 'CNY':0.1,
                    'COP':0.000175, 'CZK':0.03, 'DKK':0.11, 'EEK':0, 'EGP':0.04, 'EUR':1.17, 'GBP':0.81, 'HKD':0.08,
                    'HUF':0.002, 'IDR':0.000042, 'INR':0.01, 'ISK':0.0053, 'ITL':0, 'JPY':0.007, 'KRW':0.000633, 'LTL':0.25,
                    'NOK':0.11, 'NZD':0.66, 'PEN':0.28, 'PHP':0.02, 'LVL':1.23, 'MXN':0.03, 'MYR':0.16, 'NGN':0.0026,
                    'PKR':0.006, 'PLN':0.25, 'RUR':0.01, 'SEK':0.11, 'SGD':0.73, 'THB':0.03, 'TRL':0.13, 'TWD':0.03,
                    'UAH':0.04, 'VEB':0.1, 'ZAR':0.06}
    x = str(x)
    x = x.replace(',', '').replace('$','')
    x = x.lstrip()


    if x.isdigit() == True:
        return float(x)

    country_code = x[:3]
    if country_code in list_of_curr:
        return (float(x[3:len(list(x))]) * list_of_curr[f'{country_code}'])



def find_currencies(x):
        '''
           When given a iterable with strings having the leading 3-letter country code followed by a numerical value, return a list of the unique currency abbreviations found.

        Parameters
        ----------
        A column or list containing the strings in the format: 'AUD160,000,000'


        Returns
        -------

        List of unique 3-letter currency abbreviations.


        Examples
        --------

        >>> find_currencies(df['currency_column'])
        [RUR, PLN, SEK, SGD, THB]
        '''
        import numpy as np

        currencies = []
        for i in x:
            if i[:3].isalpha():
                currencies.append(i[:3])
                return np.unique(currencies)



def clean_currency(x):
        '''
           Checks if argument is a string, then removes dollar signs and commas.

        Parameters
        ----------
        A string containing a dollar sign or comma.


        Returns
        -------

        String with commas and dollar signs removed.



        Examples
        --------

        >>> clean_currency('$160,000,000')
        '160000000'
        '''
        if isinstance(x, str):
            x = x.replace('$', '').replace(',', '')
            return x
        return(x)

def parse_country(country) -> dict:
    """ Parse the database results into a Python dictionary """

    return {
        'name': country.get('name'),
        'confirmed': country.get('confirmed'),
        'deaths': country.get('deaths'),
        'active': country.get('active'),
        'recovered': country.get('recovered'),
        'last_updated_by_source_at': country.get('last_updated_by_source_at')
    }

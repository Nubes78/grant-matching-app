
def match_grants_to_businesses(grants, businesses):
    matches = []
    for grant in grants:
        for business in businesses:
            if grant["technology"] == business["industry"]:
                matches.append({"grant": grant["title"], "business": business["name"]})
    return matches

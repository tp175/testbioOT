# CLI for OpenTargetsClient #

import sys
import click

@click.command()
@click.option('-t', help='Target ID', required=False, type=str, default="")
@click.option('-d', help='Disease ID', required=False, type=str, default="")

def main(t, d):

    # Quick Check - arguments (none/both)
    if t == '' and d == '':sys.exit(1)
    if t != '' and d != '':sys.exit(1)

    # Load Func re opentargets querying ( pip install opentargets )
    # https://opentargets.readthedocs.io/en/stable/index.html
    from opentargets import OpenTargetsClient
    ot = OpenTargetsClient()
    # dir(ot)

    # Define Func re statistical analyses
    def doScoreStats(search_score):

        import statistics
        print('-----')
        print('Max:', max(search_score))
        print('Min:', min(search_score))
        print('Ave:', statistics.mean(search_score))
        print('SD:', statistics.stdev(search_score))

    # Run Analysis re TARGET (t)
    if t != '':

        search_id = t;
        a_for_target = ot.get_associations_for_target(search_id)

        # Quick Check - correct 'target' queried
        if a_for_target.info['query']['target'] == [search_id]:

            search_score = []  # initialise list

            # Loop Over Entries
            for a in a_for_target:
                search_score.append(a['association_score']['overall'])
                print(a['target']['id'], a['disease']['id'], a['association_score']['overall'])

            doScoreStats(search_score)

        else:
            print("please check match (exited) -", [search_id], " vs ", a_for_target.info['query']['target'])
            sys.exit(1)

    # Run Analysis re DISEASE (d)
    elif d != '':

        search_id = d
        a_for_disease = ot.get_associations_for_disease(search_id)

        # Quick Check - correct 'disease' queried
        if a_for_disease.info['query']['disease'] == [search_id]:

            search_score = []  # initialise list

            # Loop Over Entries
            for a in a_for_disease:
                search_score.append(a['association_score']['overall'])
                print(a['target']['id'], a['disease']['id'], a['association_score']['overall'])

            doScoreStats(search_score)

        else:
            print("please check match (exited) - ", [search_id], " vs ", a_for_disease.info['query']['disease'])
            sys.exit(1)

# xxx
if __name__ == '__main__':
    main()
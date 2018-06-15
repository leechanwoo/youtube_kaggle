
import csv
import os



def make_iterator(path, select_col=None, row_limit=None):
    with open(path, 'r') as f:
        data = csv.reader(f, delimiter=',')
        for i, row in enumerate(data):
            if row_limit != None:
                if i > row_limit:
                    break

            if i == 0:
                num_col = row.index(select_col)
            yield row[num_col]




def counter(_iter, name='untitled'):
    next(_iter)
    counter_dict = {}
    for k in _iter:
        if k in counter_dict:
            counter_dict[k] += 1
        else:
            counter_dict[k] = 1

    sorted_keys = sorted(counter_dict, key=counter_dict.__getitem__, reverse=True)
    sum_values = float(sum(counter_dict.values()))

    print(name)
    print('\n'.join(['{}:  {}  {}%'.format(str(k), str(counter_dict[k]), round(float(counter_dict[k])/sum_values*100.0), 2) for k in sorted_keys]))
    print()


def main():
    data_path = '/Users/chanwoo/Repositories/youtube/datasets/stack-overflow-2018-developer-survey/'
    public = 'survey_results_public.csv'
    public_data = os.path.join(data_path, public)
#    interest_column = ['OpenSource', 'Country', 'Student', 'Employment', 'YearsCoding', 'JobSatisfaction', 'IDE', 'NumberMonitors', 'VersionControl', 'WakeTime', 'Age']
    interest_column = ['OpenSource', 'Country', 'Student', 'Employment', 'YearsCoding', 'JobSatisfaction', 'NumberMonitors', 'VersionControl', 'WakeTime', 'Age']


    for c in interest_column:
        opensource = make_iterator(public_data, row_limit=None, select_col=c)
        counter(opensource, c)





if __name__ == '__main__':
    main()

import os
import shutil


TXT_FILE = 'list.txt'
RLS_DIR = 'C:\\rootdest\\'
RLS_UNSORTED_DIR = 'C:\\srcdir\\'


def parse_release(line):
    splitted = line.split()
    return splitted[1], splitted[-1]


def parse_releases(txt_file):
    with open(txt_file, 'r') as handle:
        for line in handle:
            yield parse_release(line)


def parse_date(date):
    return date.strip('[]').split('-')


def release_exists_on_hdd(release):
    return os.path.exists(os.path.join(RLS_UNSORTED_DIR, release))


def get_sorted_dir(release, date):
    year, month, day = parse_date(date)
    return os.path.join(RLS_DIR, year, '{0}{1}'.format(month, day))


def main():
    for release, date in parse_releases(TXT_FILE):

        if release_exists_on_hdd(release):
            sorted_dir = get_sorted_dir(release, date)

            if not os.path.exists(sorted_dir):
                os.makedirs(sorted_dir)

            unsorted_dir = os.path.join(RLS_UNSORTED_DIR, release)
            sorted_release = os.path.join(sorted_dir, release)

            if os.path.exists(sorted_release):
                print 'Skipping {0} because path already exists ...'.format(release, sorted_dir)
            else:
                print 'Moving {0} to {1} ...'.format(release, sorted_dir)
                
                shutil.move(unsorted_dir, sorted_release)

                


if __name__ == '__main__':
    main()
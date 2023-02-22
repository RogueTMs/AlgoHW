import git
import os
import subprocess


def solution(repo, hash_from, hash_to, file):
    rev = '%s..%s' % (hash_from, hash_to)
    commits = list(map(str, list(repo.iter_commits(rev=rev))[::-1]))
    cur = -1
    l_ind = 0
    r_ind = len(commits)

    os.chdir('Repo')
    while l_ind <= r_ind:
        cur = (l_ind + r_ind) // 2
        check = repo.git.show('%s:%s' % (commits[cur], file))

        try:
            subprocess.run(['python', '-c', check], check=True, capture_output=True)
            l_ind = cur + 1
        except subprocess.CalledProcessError:
            r_ind = cur - 1

    os.chdir('..')
    return commits[cur]


c_rep = git.Repo.clone_from('https://github.com/RogueTMs/Repo_for_test_bisect.git', 'Repo')

print(
    solution(c_rep, 'd1fce72b12cbdbe35b034ce3571bafb6295161b7',
             'f08ec3a6e36eb973941a9ce917fe82c76f0c8994', 'Main.py'))

git.rmtree('Repo')

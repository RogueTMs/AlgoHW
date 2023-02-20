import git


def solution(path, branch, hash_from, hash_to, file):
    repo = git.Repo.clone_from(path, 'Repo')
    commits = list(map(str, list(repo.iter_commits(branch))[::-1]))
    cur = -1

    l_ind, r_ind = -1, -1

    for i in range(len(commits)):
        if hash_from == commits[i]:
            l_ind = i
        if hash_to == commits[i]:
            r_ind = i

    if l_ind == -1 or r_ind == -1:
        print("Incorrect hash")
        git.rmtree('Repo')
        exit(0)

    while l_ind <= r_ind:
        cur = (l_ind + r_ind) // 2
        check = repo.git.show("%s:%s" % (commits[cur], file))
        comp = compile(check, 'mulstring', 'exec')
        print(cur, l_ind, r_ind)
        try:
            exec(comp)
            l_ind = cur + 1
        except:
            r_ind = cur - 1

    git.rmtree('Repo')
    return commits[cur + 1]


print(
    solution('https://github.com/RogueTMs/Repo_for_test_bisect.git', 'main', 'd1fce72b12cbdbe35b034ce3571bafb6295161b7',
             'f08ec3a6e36eb973941a9ce917fe82c76f0c8994', 'Main.py'))

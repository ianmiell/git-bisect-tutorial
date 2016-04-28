from shutit_module import ShutItModule

class git_bisect_tutorial(ShutItModule):

	def build(self, shutit):
		shutit.send('cd /myproject')
		shutit.challenge(
			'''In this tutorial you will be asked to find the commit that
introduced a bug!

You are given a git repo with a 1024-commit history, and a script (test.sh)
that tells you whether the repo is in an 'OK' or 'FAIL'ed state.

Rather than going through each commit in order you are going to find the
breaking commit using git bisect.

You have a full bash shell, so can use vi, less, man etc..

If any tools are missing or there are bugs raise a github request or contact
@ianmiell on twitter.

CTRL-] (right angle bracket) to continue.
''',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['Hit CTRL-]'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'echo 1',
				'context':'docker',
				'reset_container_name':'imiell/git-bisect-tutorial:step_10',
				'ok_container_name':'imiell/git-bisect-tutorial:step_10'
			}
		)
		shutit.challenge(
			'''We are at the HEAD of the repo in a broken state. You can
run './test.sh' to see the output if you want, and/or have a look at the
history with a 'git log'.

Your first challenge is to start your git bisect session!''',
			'git bisect start',
			challenge_type='golf',
			expect_type='exact',
			hints=['man git bisect','git bisect start'],
			congratulations='OK! git bisect session has been started',
			follow_on_context={
				'check_command':'git bisect log',
				'context':'docker',
				'reset_container_name':'imiell/git-bisect-tutorial:step_10',
				'ok_container_name':'imiell/git-bisect-tutorial:step_11'
			}
		)
		shutit.challenge(
			'''You have started the git bisect session.

Now you need to tell git two things: a point in the history where you know the
state is bad, and a point where it was good.

You know this point is bad, because there's a bug on HEAD.

Mark this point as bad.
''',
			'5aaf8153403bd7a920ec234b31703fd5',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['man git bisect','git bisect bad'],
			congratulations='OK! HEAD marked as bad',
			follow_on_context={
				'check_command':'git bisect log',
				'context':'docker',
				'reset_container_name':'imiell/git-bisect-tutorial:step_11',
				'ok_container_name':'imiell/git-bisect-tutorial:step_12'
			}
		)
		shutit.challenge(
			'''You have told git where a bad commit is. Now you need to 
give it a good one.

To make things simple, check out the initial commit in the history, which
you know is good. If you're not sure, run ./test.sh to check.

When that's done, mark it as good.
''',
			'3ef3328cb3130c78e52b84d6f1782461',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['There are 1024 commits in the history','git checkout HEAD~n','git checkout HEAD~1023'],
			congratulations='OK! First commit marked as good!',
			follow_on_context={
				'check_command':'git bisect log',
				'context':'docker',
				'reset_container_name':'imiell/git-bisect-tutorial:step_12',
				'ok_container_name':'imiell/git-bisect-tutorial:step_14'
			}
		)
		shutit.challenge(
			'''git bisect is now set up.

You will have noticed how git bisect has moved you within the repository
to the middle point of its history. Yes, it's bisected between the good and
bad points, and is asking you whether this point is ok before bisecting again.

Run 'git bisect log' at any point to get a summary of where you are in the
bisection process.

Now you're on your own! Keep marking the points as either good or bad until
git bisect tells you you're done. When you're done, hit CTRL-] as normal!
''',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['Run ./test.sh, and then input git bisect good or bad depending on whether it passed or failed.'],
			congratulations='OK! git bisect complete, you have found the error. Run "git bisect log" to see the results.',
			follow_on_context={
				'check_command':'git bisect log | grep first | wc -l',
				'context':'docker',
				'reset_container_name':'imiell/git-bisect-tutorial:step_14',
				'ok_container_name':'imiell/git-bisect-tutorial:step_24'
			}
		)
		shutit.pause_point('Feel free to continue experimenting...')
		return True
	

	

def module():
	return git_bisect_tutorial(
		'tk.shutit.git_bisect_tutorial', 1845506479.0001,
		description='Git bisect tutorial',
		maintainer='ian.miell@gmail.com',
		delivery_methods=['docker'],
		depends=['shutit.tk.setup']
	)

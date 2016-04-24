from shutit_module import ShutItModule

class git_bisect_tutorial(ShutItModule):

	def build(self, shutit):
		shutit.send('cd /myproject')
		shutit.challenge(
			'''In this tutorial you will be asked to TODO

You have a full bash shell, so can use vi, less, man etc..

If any tools are missing or there are bugs raise a github request or contact
@ianmiell on twitter.

CTRL-] (right angle bracket) to continue.
''',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['Hit CTRL-C'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'echo 1',
				'context':'docker',
				'reset_container_name':'imiell/git-bisect-tutorial:step_TODO',
				'ok_container_name':'imiell/git-bisect-tutorial:step_TODO'
			}
		)

# STEPS TODO:
git bisect start
./test.sh 
git bisect bad
git checkout HEAD~1023
./test.sh 
git bisect good
./test.sh 
git bisect good
./test.sh 
git bisect bad
./test.sh 
[...]
check with git status
		return True
	

def module():
	return git_bisect_tutorial(
		'tk.shutit.git_bisect_tutorial', 1845506479.0001,
		description='Git bisect tutorial',
		maintainer='ian.miell@gmail.com',
		delivery_methods=['docker'],
		depends=['shutit.tk.setup']
	)

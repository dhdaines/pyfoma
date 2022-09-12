import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
	long_description = fh.read()

github_permalink = "https://raw.githubusercontent.com/mhulden/pyfoma/main/docs/images/"
fixed_readme = long_description.replace("./docs/images/", github_permalink)

setuptools.setup(
	name = "pyfoma",
	version = "v0.1.0-alpha.7",
	author = "Mans Hulden",
	author_email = "mans.hulden@colorado.edu",
	description = "Python Finite-State Toolkit",
	long_description = fixed_readme,
	long_description_content_type = "text/markdown",
	url = "https://github.com/mhulden/pyfoma",
	project_urls = {
		"Bug Tracker": "https://github.com/mhulden/pyfoma/issues",
	},
	classifiers = [
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: Apache Software License",
		"Operating System :: OS Independent",
	],
	py_modules = ["pyfoma"],
	python_requires = ">=3.6",
	install_requires = [
		"graphviz<0.16", "IPython"
	]
)

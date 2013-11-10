from willie import coretasks
from willie.module import commands
import os
import subprocess


def configure(config):
    """
    | [document] | example | purpose |
    | ---------- | ------- | ------- |
    | layout | default | The jekyll layout to use for the commands page |
    | base_dir | /home/user/willie-website | The location of the jekyll site source |
    | plugins_dir | /home/user/willie-website/_plugins | The location of the jekyll plugins directory |
    | layouts_dir | /home/user/willie-website/_layouts | The location of the jekyll layouts directory |
    | output_dir | /var/www/willie | The location of the jekyll generated site |
    | jekyll_location | /opt/jekyll/jekyll | The location of the jekyll executable. Not needed if jekyll is on the user's PATH |
    """
    if config.option('Compile command listings to a Jekyll site', False):
        config.add_section('document')
        config.interactive_add('document', 'layout',
            'The jekyll layout to use for the commands page')
        config.interactive_add('document', 'base_dir',
            'The location of the jekyll site source ')
        config.interactive_add('document', 'plugins_dir',
            'The location of the jekyll plugins directory')
        config.interactive_add('document', 'layouts_dir',
            'The location of the jekyll layouts directory')
        config.interactive_add('document', 'output_dir',
            'The location of the jekyll generated site')
        config.interactive_add('document', 'jekyll_location',
            "The location of the jekyll executable. Not needed if jekyll is on"
            " the user's PATH.")


def setup(bot):
    if not bot.config.document.base_dir:
        raise ConfigurationError('Must provide Jekyll base_dir')


@commands('document')
def document(bot, trigger):
    conf = bot.config.document
    layout = conf.layout or 'default'
    base_dir = conf.base_dir
    output_dir = conf.output_dir or os.path.join(base_dir, '_site')
    plugins_dir = conf.plugins_dir or os.path.join(base_dir, 'plugins')
    layouts_dir = conf.layouts_dir or os.path.join(base_dir, '_layouts')

    with open(os.path.join(base_dir, 'modules.md'), 'w') as f:
        front_matter = '''---\nlayout: {}\ntitle: {} commands list\n---\n\n'''
        f.write(front_matter.format(layout, bot.nick))
        f.write('| Command | Purpose | Example |\n')
        f.write('| ------- | ------- | ------- |\n')

        for command in sorted(bot.doc.iterkeys()):
            doc = bot.doc[command]
            docstring = doc[0].replace('\n\n', '<br />').replace('\n', ' ')
            f.write('| {} | {} | {} |\n'.format(command, docstring, doc[1]))
    command = "{} build -s {} -d {} -p {} --layouts {}"
    command = command.format(conf.jekyll_location or 'jekyll', base_dir,
        output_dir, plugins_dir, layouts_dir)
    print command
    subprocess.call(command.split(' '))
    bot.say('Finished processing documentation.')

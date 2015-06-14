# jbosstools-oomph

oomph project catalog for jbosstools modules

Main file is in setup/jbosstools.setup

To use:

. Run oomph installer
. Switch to advanced
. Drag'n'drop setup/jbosstools.setup to github.com/User folder
. Double click on each module you want to include in your setup

To generate from templates:

----
pip install cheetah
python generate-oomph.py
----

The file `modules.yml` is what is used to generate oomph templates
for all JBoss Tools modules.


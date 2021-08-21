# ALBI-345

This is a **nikola** static website for my AL/BI General Entomology course which I teach at the University of Guam.

The site is publicly available on **github pages** at https://aubreymoore.github.io/ALBI-345/.

## Editing the Site ##
To edit the site, I run **nikola** in a **docker** container.

    sudo docker run -ti -p 127.0.0.1:8008:8000 -v /home/aubrey/ALBI-345:/ALBI-345 aubreymoore/nikola
    cd ALBI-345
    git config credential.helper store

### Notes ###

* When the above command line is run for the first time, my **aubreymoore/nikola** docker image will be downloaded from **dockerhub**. On subsequent runs, a container will be started using the downloaded image stored on my local machine.
* The **-v** argument loads the site as a **docker volume**. This allows me to edit the site using any software installed on my local machine. Once edits are done, rebuild the site using **nikola build**. I can then preview the site in my browser at **127.0.0.1:8008**.
* When finished editing, I type **exit** to leave the container. I then use **git** to commit and push as usual.

      git status
      git add .
      git commit -m 'minor changes'
      git push

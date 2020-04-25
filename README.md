# LaurieOnTracking
Laurie's code for reading and working with Metrica's tracking and event data.

The sample data can be found in Metrica's github repository here: https://github.com/metrica-sports/sample-data

We'll be updating this repo as the friends of tracking series develops, adding code for measuring player velocity and acceleration, measuring team formations, and evaluating pitch control using a model published by Will Spearman. 

To create movies from the tracking data you'll need to have ffmpeg installed. You can do this by following the instructions here: https://anaconda.org/conda-forge/ffmpeg (you may need to restart python afterwards).

## Notebooks
If you want to run the notebooks for each session, you can either install the repository locally or run it directly on Binder or Google Colab. In case you do not know, use Google Colab!  
- Run each cell in the notebook and ignore the warning about the unknown environment.
- The data is downloaded directly from Metricas repository.  
- Give it some time when it says "Readining team home" in a cell.

| Lesson | Binder | Colab |
| --- | --- | --- |
| [Lesson 4 - Basic Plotting of Event and Tracking Data](notebooks/Lesson4.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/seidlr/LaurieOnTracking/master?filepath=notebooks/Lesson4.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seidlr/LaurieOnTracking/blob/master/notebooks/Lesson4.ipynb) |
| [Lesson 5 - Advanced Plotting and Summary Statistics](notebooks/Lesson5.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/seidlr/LaurieOnTracking/master?filepath=notebooks/Lesson5.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seidlr/LaurieOnTracking/blob/master/notebooks/Lesson5.ipynb) |
| [Lesson 6 - Pitch Control](notebooks/Lesson6.ipynb) | [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/seidlr/LaurieOnTracking/master?filepath=notebooks/Lesson6.ipynb) |  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/seidlr/LaurieOnTracking/blob/master/notebooks/Lesson6.ipynb) |
 


### Local installation
1. Download Anaconda
2. Clone repository
3. Create environment `fotd-laurie-on-tracking`:
```
conda env update
```
4. Start jupyter notebook server
```
jupyter notebook
```
5. Select the kernel `fotd-laurie-on-tracking` for your notebook
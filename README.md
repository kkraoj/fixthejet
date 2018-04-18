# fixthejet
This script allows you to change an image (.jpg/.png) file made with _jet_ colormap to any other colormap of your choice. The script selectively changes _jet_ colors only. All others colors in the image remain unchanged (including background and text). 

## Running

`python fixthejet.py --input <input file> --output <output file>`

Use `--colormap <output colormap>` to control colormap of outfile. Default is _viridis_. Only Matplotlib colormaps supported. 

### Prerequisites

Python 3

## Example 1

`python fixthejet.py --input .\images\SST.png --output .\images\SST_viridis.png`

### Input file
![input1](images/SST.png) 

### Output file
![output1](images/SST_viridis.png)

## Example 2

`python fixthejet.py --input .\images\cube.png --output .\images\cube_plasma.png --colormap plasma` 

### Input file

![input2](images/cube.png)

### Output file

![output2](images/cube_plasma.png)

## Example 3

`python fixthejet.py --input .\images\cone.jpg --output .\images\cone_inferno.jpg --colormap inferno` 

### Input file

![input2](images/cone.jpg)

### Output file

![output2](images/cone_inferno.jpg)


## License
* Do not own Copyright. Original works belongs to [Carreau](https://github.com/Carreau)

## Acknowledgments

* Forked from [viridisify](https://github.com/Carreau/miscs/blob/master/Viridisify.ipynb)

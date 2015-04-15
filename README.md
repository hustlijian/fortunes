code to crawl data to generate fortune data file.

## inspire

inspire by [ruanyf](https://github.com/ruanyf/fortunes)

## requirement

- [requests](http://docs.python-requests.org/en/latest/)
- [beautiful soup](http://www.crummy.com/software/BeautifulSoup/)

## install

    git clone https://github.com/hustlijian/fortunes.git
    cd fortunes
    sudo pip install -r requirements.txt

## build data

    ./build.sh 

## install fortune and copy data file

    # Debian/Ubuntu
    $ sudo apt-get install fortune
    $ sudo cp data/* /usr/share/games/fortunes/

    # Mac
    $ brew install fortune
    $ sudo cp data/* /usr/local/Cellar/fortune/9708/share/games/fortunes

ruby -v && gem -v && gcc -v && g++ -v && make -v &&
apt-get install ruby-full build-essential zlib1g-dev
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
#the following line is ok if ruby is 2.6
gem install jekyll bundler github-pages
#gem install jekyll bundler -- --disable-lto

bundle update

## Run following manually
#mkdir avoco
#cd avoco
#jekyll new .
##bundle exec jekyll VERSION new .
#
##change lines in Gemfile to use github-pages, and remove jekyll
#bundle update
## test locally
#bundle exec jekyll serve

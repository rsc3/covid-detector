#Create new env with conda libgcc
conda create -n ORFfinder -c anaconda libgcc
source activate ORFfinder

#Setup scripts to set LD_LIBRARY_PATH
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
mkdir -p $CONDA_PREFIX/etc/conda/deactivate.d

cat <<EOF >$CONDA_PREFIX/etc/conda/activate.d/LD_PATH.sh
export LD_LIBRARY_PATH_CONDA_BACKUP=$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH
EOF

cat <<EOF >$CONDA_PREFIX/etc/conda/deactivate.d/LD_PATH.sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH_CONDA_BACKUP
EOF

#Download ORFinder from NCBI
cd ~
wget ftp://ftp.ncbi.nlm.nih.gov/genomes/TOOLS/ORFfinder/linux-i64/ORFfinder.gz
gunzip ORFfinder.gz
chmod a+x ORFfinder
mv ORFfinder $CONDA_PREFIX/bin

#Re-activate to set LD_LIBRARY_PATH
source deactivate ORFfinder
source activate ORFfinder

#Test
ORFfinder
#
# Copyright (C) 2016-2017 Mellanox Technologies, Inc.
#                         All rights reserved.
# $COPYRIGHT$
#
# Additional copyrights may follow
#
# $HEADER$
#

#!/bin/bash

sourc ../env.sh

if [ -z "$SLURM_BASE" ]; then
    SLURM_BASE=/tmp/slurm_deploy/slurm/
fi
SRUN=$SLURM_BASE/bin/srun

export OMPI_MCA_PML="ucx"
export OMPI_MCA_BTL="self"
$SRUN  --mpi=pmix `dirname $0`/pmix_probe $@

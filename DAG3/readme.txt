-----------------build and run 1st container----------------
cd p1
docker build -t loop-container .
docker run loop-container

-----------------build and run 2nd container----------------
cd p2
docker build -t sort-container .
docker run sort-container

-----------------build and run 3rd container----------------
cd p3
docker build -t nestloop-container .
docker run nestloop-container
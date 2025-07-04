int* countPoints(int** points, int pointsSize, int* pointsColSize,
                 int** queries, int queriesSize, int* queriesColSize,
                 int* returnSize) {
    int size = 0;
    int rSize = pointsSize;
    int* result = calloc(queriesSize, sizeof(int));

    for (int i = 0; i < queriesSize; i++) {
        int count = 0;
        
        /* NOTE check pointsColSize */
        int originX = queries[i][0];
        int originY = queries[i][1];
        int radius = queries[i][2];

        for (int j = 0; j < pointsSize; j++) {

            /* NOTE check queriesColSize */
            int pointX = points[j][0];
            int pointY = points[j][1];

            int x2 = (pointX - originX) * (pointX - originX);
            int y2 = (pointY - originY) * (pointY - originY);

            /* check point is inside circle */
            if (x2 + y2 <= radius * radius) {
                count++;
            }
        }

        result[size++] = count;
        *returnSize = size;
    }

    return result;
}

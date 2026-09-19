#include <stdio.h>

struct point {
    int x;
    int y;
};

/// Return square distance between closest point on a rectangle to point
/// @param min_pt rectangle min point
/// @param max_pt rectangle max point
/// @param pt point
/// @return square distance
static int sq_dist_point_rectangle(struct point min_pt, struct point max_pt, struct point pt) {
    int sq_dict = 0;

    // x
    if (pt.x < min_pt.x) {
        sq_dict += (min_pt.x - pt.x) * (min_pt.x - pt.x);
    }

    if (pt.x > max_pt.x) {
        sq_dict += (pt.x - max_pt.x) * (pt.x - max_pt.x);
    }

    // y
    if (pt.y < min_pt.y) {
        sq_dict += (min_pt.y - pt.y) * (min_pt.y - pt.y);
    }

    if (pt.y > max_pt.y) {
        sq_dict += (pt.y - max_pt.y) * (pt.y - max_pt.y);
    }

    return sq_dict;
}

/// Check for overlapping between a circle and a rectangle's min and max point
/// @param radius circle radius
/// @param origin circle origin x y
/// @param min_pt rectangle min point x y
/// @param max_pt rectangle max point x y
static int check_overlap(int radius, struct point origin, struct point min_pt, struct point max_pt) {
    return  sq_dist_point_rectangle(min_pt, max_pt, origin) <= radius * radius ? 1 : 0;
}

static void test_case(struct point origin, int radius, struct point min_pt, struct point max_pt, int expected) {
    const int overlap = check_overlap(radius, origin, min_pt, max_pt);
    if (overlap == expected) {
        printf("PASS: Circle is overlapping rectangle!\n");
    } else {
        printf("FAIL: Circle is not overlapping rectangle!\n");
    }
}

int main(void) {
    printf("1401. Circle and Rectangle Overlapping\n");

    test_case(
        (struct point){.x = 0, .y = 0},
        1, 
        (struct point){.x = 1, .y = -1},
        (struct point){.x = 3, .y = 1},
        1
    );

    return 0;
}

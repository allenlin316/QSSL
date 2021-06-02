import numpy as np


def results_updated_nobatchnorm():
    accs = np.array([[[(33.52, (0, 0)), (35.4, (0, 10)), (38.14, (0, 20)), (38.98, (0, 30)), (41.08, (0, 40)),
                       (43.26, (0, 50)), (43.98, (0, 60)), (42.84, (0, 70)), (43.56, (0, 80)), (43.66, (0, 90)),
                       (45.5, (1, 0)), (47.26, (2, 0)), (50.36, (3, 0)), (50.48, (4, 0)), (48.84, (5, 0)),
                       (52.4, (6, 0)), (52.08, (7, 0)), (51.8, (8, 0)), (51.52, (9, 0))],
                      [(29.62, (0, 0)), (36.22, (0, 10)), (35.34, (0, 20)), (36.76, (0, 30)), (38.66, (0, 40)),
                       (40.58, (0, 50)), (41.78, (0, 60)), (43.2, (0, 70)), (44.62, (0, 80)), (44.52, (0, 90)),
                       (45.44, (1, 0)), (48.0, (2, 0)), (48.86, (3, 0)), (51.52, (4, 0)), (52.74, (5, 0)),
                       (53.12, (6, 0)), (52.62, (7, 0)), (54.48, (8, 0)), (52.6, (9, 0))],
                      [(30.18, (0, 0)), (37.56, (0, 10)), (36.74, (0, 20)), (38.3, (0, 30)), (40.12, (0, 40)),
                       (39.06, (0, 50)), (42.04, (0, 60)), (43.3, (0, 70)), (44.24, (0, 80)), (44.44, (0, 90)),
                       (45.98, (1, 0)), (48.0, (2, 0)), (51.56, (3, 0)), (51.2, (4, 0)), (50.92, (5, 0)),
                       (50.74, (6, 0)), (51.2, (7, 0)), (52.96, (8, 0)), (53.36, (9, 0))]],
                     [[(26.36, (0, 0)), (32.08, (0, 10)), (34.42, (0, 20)), (34.36, (0, 30)), (32.94, (0, 40)),
                       (34.72, (0, 50)), (35.34, (0, 60)), (34.18, (0, 70)), (34.1, (0, 80)), (33.66, (0, 90)),
                       (37.48, (1, 0)), (39.92, (2, 0)), (42.0, (3, 0)), (38.72, (4, 0)), (43.04, (5, 0)),
                       (44.48, (6, 0)), (44.48, (7, 0)), (47.02, (8, 0)), (46.06, (9, 0))],
                      [(27.12, (0, 0)), (36.58, (0, 10)), (38.8, (0, 20)), (41.76, (0, 30)), (40.54, (0, 40)),
                       (41.76, (0, 50)), (43.6, (0, 60)), (43.0, (0, 70)), (42.12, (0, 80)), (40.44, (0, 90)),
                       (42.38, (1, 0)), (42.28, (2, 0)), (44.96, (3, 0)), (49.76, (4, 0)), (49.84, (5, 0)),
                       (49.0, (6, 0)), (50.2, (7, 0)), (48.76, (8, 0)), (50.8, (9, 0))],
                      [(29.06, (0, 0)), (33.22, (0, 10)), (36.0, (0, 20)), (36.76, (0, 30)), (37.4, (0, 40)),
                       (39.6, (0, 50)), (39.68, (0, 60)), (38.64, (0, 70)), (40.22, (0, 80)), (39.42, (0, 90)),
                       (40.14, (1, 0)), (43.54, (2, 0)), (44.66, (3, 0)), (44.94, (4, 0)), (45.3, (5, 0)),
                       (46.64, (6, 0)), (48.76, (7, 0)), (48.96, (8, 0)), (48.38, (9, 0))]],
                     [[(40.5, (0, 0)), (45.86, (0, 10)), (48.76, (0, 20)), (48.46, (0, 30)), (50.06, (0, 40)),
                       (51.18, (0, 50)), (50.06, (0, 60)), (52.2, (0, 70)), (53.34, (0, 80)), (53.78, (0, 90)),
                       (52.96, (1, 0)), (55.66, (2, 0)), (56.4, (3, 0)), (56.84, (4, 0)), (59.12, (5, 0)),
                       (58.04, (6, 0)), (59.28, (7, 0)), (59.16, (8, 0)), (59.84, (9, 0))],
                      [(41.18, (0, 0)), (44.64, (0, 10)), (47.16, (0, 20)), (48.18, (0, 30)), (49.38, (0, 40)),
                       (49.98, (0, 50)), (51.36, (0, 60)), (52.22, (0, 70)), (52.92, (0, 80)), (52.64, (0, 90)),
                       (52.6, (1, 0)), (55.8, (2, 0)), (57.04, (3, 0)), (56.04, (4, 0)), (57.8, (5, 0)),
                       (57.86, (6, 0)), (58.36, (7, 0)), (59.08, (8, 0)), (60.14, (9, 0))],
                      [(41.24, (0, 0)), (46.0, (0, 10)), (47.22, (0, 20)), (48.58, (0, 30)), (49.84, (0, 40)),
                       (49.8, (0, 50)), (50.46, (0, 60)), (50.54, (0, 70)), (52.28, (0, 80)), (52.52, (0, 90)),
                       (53.02, (1, 0)), (56.38, (2, 0)), (55.62, (3, 0)), (57.32, (4, 0)), (57.48, (5, 0)),
                       (58.84, (6, 0)), (58.74, (7, 0)), (57.62, (8, 0)), (59.54, (9, 0))]],
                     [[(31.04, (0, 0)), (41.64, (0, 10)), (42.98, (0, 20)), (43.8, (0, 30)), (45.44, (0, 40)),
                       (46.28, (0, 50)), (46.68, (0, 60)), (48.82, (0, 70)), (49.18, (0, 80)), (49.0, (0, 90)),
                       (49.02, (1, 0)), (52.04, (2, 0)), (53.84, (3, 0)), (54.84, (4, 0)), (56.62, (5, 0)),
                       (55.88, (6, 0)), (56.92, (7, 0)), (56.62, (8, 0)), (56.74, (9, 0))],
                      [(30.74, (0, 0)), (39.6, (0, 10)), (43.1, (0, 20)), (45.14, (0, 30)), (46.14, (0, 40)),
                       (46.92, (0, 50)), (49.06, (0, 60)), (50.4, (0, 70)), (49.98, (0, 80)), (50.06, (0, 90)),
                       (49.76, (1, 0)), (52.16, (2, 0)), (53.48, (3, 0)), (54.82, (4, 0)), (56.12, (5, 0)),
                       (56.96, (6, 0)), (57.08, (7, 0)), (59.0, (8, 0)), (58.34, (9, 0))],
                      [(31.86, (0, 0)), (38.46, (0, 10)), (40.12, (0, 20)), (42.12, (0, 30)), (43.44, (0, 40)),
                       (44.94, (0, 50)), (46.18, (0, 60)), (47.12, (0, 70)), (47.44, (0, 80)), (47.84, (0, 90)),
                       (48.74, (1, 0)), (53.06, (2, 0)), (54.24, (3, 0)), (53.92, (4, 0)), (54.74, (5, 0)),
                       (55.78, (6, 0)), (56.6, (7, 0)), (56.42, (8, 0)), (57.78, (9, 0))]],
                     [[(26.66, (0, 0)), (29.1, (0, 10)), (32.36, (0, 20)), (35.52, (0, 30)), (36.12, (0, 40)),
                       (38.46, (0, 50)), (35.6, (0, 60)), (35.28, (0, 70)), (35.9, (0, 80)), (36.64, (0, 90)),
                       (35.58, (1, 0)), (39.14, (2, 0)), (40.26, (3, 0)), (43.18, (4, 0)), (45.36, (5, 0)),
                       (44.1, (6, 0)), (43.08, (7, 0)), (46.08, (8, 0)), (44.92, (9, 0))],
                      [(29.44, (0, 0)), (31.36, (0, 10)), (28.82, (0, 20)), (30.66, (0, 30)), (33.82, (0, 40)),
                       (32.3, (0, 50)), (32.52, (0, 60)), (32.92, (0, 70)), (32.8, (0, 80)), (34.64, (0, 90)),
                       (33.22, (1, 0)), (40.02, (2, 0)), (43.92, (3, 0)), (42.34, (4, 0)), (41.24, (5, 0)),
                       (42.72, (6, 0)), (39.82, (7, 0)), (42.48, (8, 0)), (38.7, (9, 0))],
                      [(26.58, (0, 0)), (25.94, (0, 10)), (32.48, (0, 20)), (28.42, (0, 30)), (26.9, (0, 40)),
                       (30.4, (0, 50)), (30.02, (0, 60)), (30.48, (0, 70)), (31.54, (0, 80)), (32.96, (0, 90)),
                       (32.22, (1, 0)), (35.8, (2, 0)), (35.3, (3, 0)), (35.18, (4, 0)), (35.94, (5, 0)),
                       (32.72, (6, 0)), (29.96, (7, 0)), (34.08, (8, 0)), (33.02, (9, 0))]],
                     [[(28.98, (0, 0)), (27.82, (0, 10)), (28.48, (0, 20)), (28.72, (0, 30)), (26.12, (0, 40)),
                       (25.14, (0, 50)), (24.82, (0, 60)), (24.8, (0, 70)), (24.72, (0, 80)), (24.24, (0, 90)),
                       (24.28, (1, 0)), (25.84, (2, 0)), (25.66, (3, 0)), (26.04, (4, 0)), (26.54, (5, 0)),
                       (29.72, (6, 0)), (28.08, (7, 0)), (29.44, (8, 0)), (28.48, (9, 0))],
                      [(25.16, (0, 0)), (29.64, (0, 10)), (30.92, (0, 20)), (27.22, (0, 30)), (28.9, (0, 40)),
                       (28.24, (0, 50)), (26.7, (0, 60)), (28.92, (0, 70)), (29.8, (0, 80)), (30.66, (0, 90)),
                       (33.16, (1, 0)), (33.64, (2, 0)), (35.58, (3, 0)), (33.18, (4, 0)), (35.06, (5, 0)),
                       (35.26, (6, 0)), (35.26, (7, 0)), (40.08, (8, 0)), (34.76, (9, 0))],
                      [(24.9, (0, 0)), (28.9, (0, 10)), (27.06, (0, 20)), (21.16, (0, 30)), (22.18, (0, 40)),
                       (24.3, (0, 50)), (21.4, (0, 60)), (20.6, (0, 70)), (20.5, (0, 80)), (20.62, (0, 90)),
                       (20.7, (1, 0)), (22.94, (2, 0)), (26.92, (3, 0)), (29.04, (4, 0)), (28.76, (5, 0)),
                       (26.34, (6, 0)), (27.32, (7, 0)), (26.4, (8, 0)), (33.54, (9, 0))]]])

    widths = np.array([16, 8, 512, 32, 4, 2])

    order = widths.argsort()
    widths.sort()
    sorted_accs = accs[order]

    return widths, sorted_accs


# ResNet-18, 5 classes, 25,000 images, 100 linear probing epochs, classical, variable bottleneck, sigmoid before
# testnet, batchnorm before sigmoid
def results_updated():
    accs = np.array([[[(26.62, (0, 0)), (36.98, (0, 10)), (37.24, (0, 20)), (33.96, (0, 30)), (38.6, (0, 40)),
                       (37.58, (0, 50)), (34.84, (0, 60)), (33.14, (0, 70)), (36.48, (0, 80)), (39.88, (0, 90)),
                       (46.42, (1, 0)), (48.9, (2, 0)), (50.02, (3, 0)), (51.38, (4, 0)), (51.82, (5, 0)),
                       (51.04, (6, 0)), (51.32, (7, 0)), (50.78, (8, 0)), (53.98, (9, 0))],
                      [(31.02, (0, 0)), (37.02, (0, 10)), (38.12, (0, 20)), (39.04, (0, 30)), (41.32, (0, 40)),
                       (43.06, (0, 50)), (42.68, (0, 60)), (43.52, (0, 70)), (43.16, (0, 80)), (44.16, (0, 90)),
                       (45.48, (1, 0)), (48.8, (2, 0)), (49.62, (3, 0)), (51.94, (4, 0)), (52.74, (5, 0)),
                       (52.34, (6, 0)), (53.98, (7, 0)), (54.4, (8, 0)), (55.66, (9, 0))],
                      [(31.4, (0, 0)), (38.42, (0, 10)), (38.96, (0, 20)), (40.42, (0, 30)), (42.34, (0, 40)),
                       (42.54, (0, 50)), (43.52, (0, 60)), (44.2, (0, 70)), (46.4, (0, 80)), (45.92, (0, 90)),
                       (46.84, (1, 0)), (48.7, (2, 0)), (49.34, (3, 0)), (51.22, (4, 0)), (52.5, (5, 0)),
                       (53.86, (6, 0)), (54.6, (7, 0)), (53.94, (8, 0)), (55.1, (9, 0))]],
                     [[(31.16, (0, 0)), (35.84, (0, 10)), (34.28, (0, 20)), (32.74, (0, 30)), (35.14, (0, 40)),
                       (36.24, (0, 50)), (36.76, (0, 60)), (36.62, (0, 70)), (22.6, (0, 80)), (30.56, (0, 90)),
                       (38.22, (1, 0)), (44.24, (2, 0)), (46.46, (3, 0)), (46.7, (4, 0)), (48.12, (5, 0)),
                       (49.18, (6, 0)), (47.68, (7, 0)), (51.2, (8, 0)), (48.18, (9, 0))],
                      [(30.4, (0, 0)), (32.96, (0, 10)), (35.56, (0, 20)), (39.16, (0, 30)), (39.52, (0, 40)),
                       (40.1, (0, 50)), (39.78, (0, 60)), (39.94, (0, 70)), (40.78, (0, 80)), (41.08, (0, 90)),
                       (42.02, (1, 0)), (44.78, (2, 0)), (45.62, (3, 0)), (46.82, (4, 0)), (46.76, (5, 0)),
                       (49.34, (6, 0)), (49.72, (7, 0)), (49.9, (8, 0)), (51.46, (9, 0))],
                      [(29.14, (0, 0)), (31.28, (0, 10)), (33.06, (0, 20)), (32.94, (0, 30)), (34.04, (0, 40)),
                       (33.58, (0, 50)), (34.3, (0, 60)), (35.04, (0, 70)), (35.7, (0, 80)), (37.46, (0, 90)),
                       (37.36, (1, 0)), (41.9, (2, 0)), (45.22, (3, 0)), (42.9, (4, 0)), (43.38, (5, 0)),
                       (44.5, (6, 0)), (45.14, (7, 0)), (46.84, (8, 0)), (48.38, (9, 0))]],
                     [[(40.64, (0, 0)), (47.1, (0, 10)), (49.92, (0, 20)), (49.44, (0, 30)), (50.34, (0, 40)),
                       (50.04, (0, 50)), (51.74, (0, 60)), (52.76, (0, 70)), (52.68, (0, 80)), (53.58, (0, 90)),
                       (52.98, (1, 0)), (53.26, (2, 0)), (56.24, (3, 0)), (56.82, (4, 0)), (58.14, (5, 0)),
                       (58.52, (6, 0)), (58.98, (7, 0)), (58.94, (8, 0)), (59.86, (9, 0))],
                      [(41.58, (0, 0)), (46.48, (0, 10)), (47.92, (0, 20)), (50.06, (0, 30)), (50.14, (0, 40)),
                       (51.46, (0, 50)), (51.9, (0, 60)), (51.72, (0, 70)), (52.28, (0, 80)), (53.14, (0, 90)),
                       (53.72, (1, 0)), (56.16, (2, 0)), (55.8, (3, 0)), (56.62, (4, 0)), (57.0, (5, 0)),
                       (57.18, (6, 0)), (58.38, (7, 0)), (57.72, (8, 0)), (59.48, (9, 0))],
                      [(38.64, (0, 0)), (44.78, (0, 10)), (48.06, (0, 20)), (49.98, (0, 30)), (51.24, (0, 40)),
                       (51.74, (0, 50)), (52.98, (0, 60)), (52.9, (0, 70)), (53.32, (0, 80)), (53.58, (0, 90)),
                       (53.64, (1, 0)), (55.78, (2, 0)), (56.0, (3, 0)), (56.8, (4, 0)), (57.82, (5, 0)),
                       (58.48, (6, 0)), (59.02, (7, 0)), (59.48, (8, 0)), (60.04, (9, 0))]],
                     [[(32.08, (0, 0)), (40.42, (0, 10)), (42.78, (0, 20)), (44.3, (0, 30)), (45.2, (0, 40)),
                       (46.54, (0, 50)), (47.38, (0, 60)), (48.72, (0, 70)), (49.76, (0, 80)), (50.26, (0, 90)),
                       (50.82, (1, 0)), (52.58, (2, 0)), (53.1, (3, 0)), (53.72, (4, 0)), (54.38, (5, 0)),
                       (55.82, (6, 0)), (56.16, (7, 0)), (56.82, (8, 0)), (56.32, (9, 0))],
                      [(32.16, (0, 0)), (38.64, (0, 10)), (41.44, (0, 20)), (43.32, (0, 30)), (45.16, (0, 40)),
                       (46.6, (0, 50)), (47.62, (0, 60)), (48.66, (0, 70)), (48.04, (0, 80)), (49.1, (0, 90)),
                       (47.78, (1, 0)), (51.42, (2, 0)), (53.5, (3, 0)), (54.44, (4, 0)), (55.06, (5, 0)),
                       (56.06, (6, 0)), (55.5, (7, 0)), (55.92, (8, 0)), (57.0, (9, 0))],
                      [(34.0, (0, 0)), (38.46, (0, 10)), (43.88, (0, 20)), (45.98, (0, 30)), (46.84, (0, 40)),
                       (47.86, (0, 50)), (48.6, (0, 60)), (48.88, (0, 70)), (49.5, (0, 80)), (49.52, (0, 90)),
                       (49.88, (1, 0)), (51.24, (2, 0)), (52.22, (3, 0)), (54.4, (4, 0)), (54.84, (5, 0)),
                       (55.24, (6, 0)), (56.74, (7, 0)), (57.36, (8, 0)), (55.98, (9, 0))]],
                     [[(24.04, (0, 0)), (30.7, (0, 10)), (31.46, (0, 20)), (31.62, (0, 30)), (32.96, (0, 40)),
                       (33.66, (0, 50)), (36.06, (0, 60)), (34.78, (0, 70)), (34.44, (0, 80)), (36.38, (0, 90)),
                       (36.14, (1, 0)), (42.62, (2, 0)), (42.96, (3, 0)), (44.54, (4, 0)), (45.38, (5, 0)),
                       (45.94, (6, 0)), (46.06, (7, 0)), (45.78, (8, 0)), (48.06, (9, 0))],
                      [(31.68, (0, 0)), (31.64, (0, 10)), (30.6, (0, 20)), (31.94, (0, 30)), (32.92, (0, 40)),
                       (30.6, (0, 50)), (34.02, (0, 60)), (33.92, (0, 70)), (33.52, (0, 80)), (35.34, (0, 90)),
                       (34.38, (1, 0)), (39.56, (2, 0)), (39.24, (3, 0)), (39.56, (4, 0)), (42.12, (5, 0)),
                       (41.6, (6, 0)), (41.14, (7, 0)), (41.08, (8, 0)), (40.64, (9, 0))],
                      [(26.1, (0, 0)), (31.14, (0, 10)), (31.94, (0, 20)), (32.54, (0, 30)), (31.2, (0, 40)),
                       (32.7, (0, 50)), (32.48, (0, 60)), (33.32, (0, 70)), (33.16, (0, 80)), (32.9, (0, 90)),
                       (33.2, (1, 0)), (34.26, (2, 0)), (36.5, (3, 0)), (35.46, (4, 0)), (36.38, (5, 0)),
                       (36.82, (6, 0)), (38.5, (7, 0)), (38.08, (8, 0)), (36.54, (9, 0))]],
                     [[(30.98, (0, 0)), (28.12, (0, 10)), (30.74, (0, 20)), (31.84, (0, 30)), (37.32, (0, 40)),
                       (35.24, (0, 50)), (37.64, (0, 60)), (39.76, (0, 70)), (38.4, (0, 80)), (37.0, (0, 90)),
                       (34.28, (1, 0)), (39.84, (2, 0)), (39.24, (3, 0)), (35.54, (4, 0)), (38.84, (5, 0)),
                       (38.24, (6, 0)), (39.64, (7, 0)), (39.56, (8, 0)), (39.18, (9, 0))],
                      [(28.58, (0, 0)), (27.88, (0, 10)), (26.44, (0, 20)), (29.62, (0, 30)), (30.08, (0, 40)),
                       (33.2, (0, 50)), (32.54, (0, 60)), (32.0, (0, 70)), (33.42, (0, 80)), (33.24, (0, 90)),
                       (32.06, (1, 0)), (34.72, (2, 0)), (37.78, (3, 0)), (36.52, (4, 0)), (35.34, (5, 0)),
                       (35.88, (6, 0)), (35.78, (7, 0)), (33.82, (8, 0)), (33.92, (9, 0))],
                      [(22.04, (0, 0)), (27.34, (0, 10)), (26.34, (0, 20)), (23.58, (0, 30)), (22.72, (0, 40)),
                       (22.04, (0, 50)), (20.76, (0, 60)), (20.8, (0, 70)), (20.7, (0, 80)), (20.74, (0, 90)),
                       (20.74, (1, 0)), (20.7, (2, 0)), (20.58, (3, 0)), (21.24, (4, 0)), (20.68, (5, 0)),
                       (20.72, (6, 0)), (20.72, (7, 0)), (20.76, (8, 0)), (20.7, (9, 0))]]])

    widths = np.array([16, 8, 512, 32, 4, 2])

    order = widths.argsort()
    widths.sort()
    sorted_accs = accs[order]

    return widths, sorted_accs


# ResNet-18, 5 classes, 25,000 images, 100 linear probing epochs, classical, variable bottleneck
def results():
    accs = np.array([
        [(33.22, 9), (37.56, 19), (27.46, 49), (31.48, 99), (35.3, 199), (36.76, 299)],
        [(53.32, 9), (54.36, 19), (59.36, 49), (65.92, 99), (70.5, 199), (72.34, 299)],
        [(45.0, 9), (46.76, 19), (51.0, 49), (37.92, 99), (41.7, 199), (43.46, 299)],
        [(59.06, 9), (61.1, 19), (64.22, 49), (67.64, 99), (70.18, 199), (71.64, 299)],
        [(52.56, 9), (55.16, 19), (60.88, 49), (62.08, 99), (63.56, 199), (64.02, 299)],
        [(56.84, 9), (57.9, 19), (60.82, 49), (66.88, 99), (68.14, 199), (70.58, 299)],
        [(61.1, 9), (62.88, 19), (62.2, 49), (64.22, 99), (68.14, 199), (70.04, 299)]])

    widths = np.array([2, 12, 4, 32, 8, 16, 512])

    order = widths.argsort()
    widths.sort()
    sorted_accs = accs[order]

    return widths, sorted_accs


def results_identity():
    accs = np.array([
        [(38.64, 9), (39.04, 19), (40.1, 49), (42.48, 99), (42.66, 199), (39.58, 299)],
        [(60.68, 9), (63.34, 19), (67.46, 49), (69.96, 99), (74.28, 199), (75.72, 299)],
        [(58.88, 9), (61.44, 19), (64.58, 49), (68.78, 99), (70.36, 199), (72.16, 299)],
        [(58.34, 9), (59.24, 19), (61.6, 49), (64.72, 99), (70.88, 199), (71.5, 299)],
        [(51.14, 9), (51.92, 19), (51.32, 49), (52.94, 99), (53.18, 199), (54.18, 299)],
        [(52.74, 9), (57.86, 19), (60.3, 49), (66.56, 99), (69.74, 199), (70.34, 299)],
        [(64.76, 9), (68.42, 19), (72.32, 49), (75.66, 99), (78.48, 199), (80.12, 299)]
    ])

    widths = np.array([2, 32, 16, 12, 4, 8, 512])

    order = widths.argsort()
    widths.sort()
    sorted_accs = accs[order]

    return widths, sorted_accs

import os

from flask import Flask
from flask import request
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import preprocessing
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)


def create_sample(release_speed):
    return {'release_speed': release_speed,
            'release_spin_rate': 0,
            'zone': 0,
            'pfx_x': 0,
            'pfx_z': 0,
            'plate_x': 0,
            'plate_z': 0,
            'vx0': 0,
            'vy0': 0,
            'vz0': 0,
            'ax': 0,
            'ay': 0,
            'pitcher': 0,
            }


def setup():
    TRAIN_SIZE = .80
    KEYS = ['pitch_type', 'release_speed', 'release_spin_rate', 'zone', 'pfx_x', 'pfx_z', 'plate_x',
            'plate_z', 'vx0', 'vy0', 'vz0','ax', 'ay', 'pitcher']
    LABELS_KEY = 'pitch_type'
    DATA_FILE = '../data/braves_pitchers_2018.csv'
    data = pd.read_csv(DATA_FILE)  # 89 Columns
    data = data.dropna(subset=KEYS)  # Delete rows with empty data points
    data = data[data.pitch_type != 'PO']
    data = data[data.pitch_type != 'KN']
    label_names = data.pitch_type.unique()
    data = data.replace({label_names[i] : i for i in range(0, len(label_names) ) })
    data = data.filter(KEYS)
    num_labels = label_names.size
    num_rows = data.shape[0]
    num_features = data.shape[1]

    train_data = data.head((int)(num_rows * TRAIN_SIZE))
    test_data = data.tail(num_rows - (int)(num_rows * TRAIN_SIZE))

    train_labels = train_data['pitch_type'].values
    test_labels = test_data['pitch_type'].values

    train_data = train_data.drop(columns=['pitch_type'])
    test_data = test_data.drop(columns=['pitch_type'])

    normalizer = preprocessing.Normalizer().fit(train_data)  # fit does nothing
    train_data = normalizer.transform(train_data)
    test_data = normalizer.transform(test_data)
    print(train_data)

    KNN = KNeighborsClassifier(n_neighbors=1)
    KNN.fit(train_data,train_labels)
    y2_KNN_model = KNN.predict(test_data)
    print(train_data.shape)
    print("KNN Accuracy :", accuracy_score(test_labels, y2_KNN_model))
    print(classification_report(test_labels, y2_KNN_model, target_names=label_names, sample_weight=None, digits=4))
    print(label_names)
    print(confusion_matrix(test_labels, y2_KNN_model))
    return [KNN, label_names, normalizer]


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    set = setup()
    model = set[0]
    label_names = set[1]
    normalizer = set[2]

    # a simple page that says hello
    @app.route('/knn')
    def hello():
        release_speed = request.args.get('release_speed', 80)
        df = pd.DataFrame(create_sample(release_speed), index=[1])
        print(df, normalizer.transform(df))
        r = model.predict(normalizer.transform(df))
        return label_names[r[0]]

    return app




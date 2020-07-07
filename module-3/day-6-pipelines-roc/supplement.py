pipe = Pipeline([('imputer', SimpleImputer()),
                 ('scaler', StandardScaler()),
                 ('clf', LogisticRegression(C=1000,
                                            max_iter=1000,
                                            solver='saga'))])

## we can access to a particular step in the pipeline

pipe.fit(X_train, y_train)
pipe.score(X_train, y_train)



param_grid = dict(scaler=['passthrough', MinMaxScaler(), Normalizer(), StandardScaler()],
                  clf = [SVC(gamma='auto'),
                         LogisticRegression(solver='lbfgs', max_iter=1000)],
                  clf__C = [0.1, 10, 100])

gs = GridSearchCV(pipe, param_grid=param_grid, cv=3, verbose=1)

gs.fit(X_train, y_train)

gs.best_params_


pipe = make_pipeline(SimpleImputer(), StandardScaler(), LogisticRegression())

pipe
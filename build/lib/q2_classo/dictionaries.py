from qiime2.plugin import (SemanticType,Plugin, Int, Float, Range, Metadata, Str, Bool,
     Choices, MetadataColumn, Categorical, List,
     Citations, TypeMatch, Numeric)
from q2_types.feature_table import FeatureTable, Composition
from q2_types.feature_data import FeatureData


regress_parameters={
     'y': MetadataColumn[Numeric],
    #Formulation parameters
    'concomitant': Bool,
    'huber'      : Bool,
    'rho'        : Float,
    'rescale'    : Bool,


    #PATH parameters :
    'PATH' : Bool,
    'PATH_numerical_method' : Str,
    'PATH_n_active'         : Int, # do something here ! for now it can be a bool !
    'PATH_lambdas'          : List[Float],
    'PATH_nlam_log'         : Int,
    'PATH_lamin_log'        : Float,


    #CV parameters :
    'CV' : Bool,
    'CV_numerical_method' : Str,
    'CV_seed'             : Int, # do something here ! for now it can be a bool !
    'CV_lambdas'          : List[Float],
    'CV_oneSE'            : Bool,
    'CV_subsets'          : Int,

    #StabSel parameters :
    'StabSel' : Bool,
    'StabSel_numerical_method' : Str,
    'StabSel_seed'             : Int, # do something here ! for now it can be a bool !
    'StabSel_lam'              : Float, # can be str as well for now !
    'StabSel_true_lam'         : Bool,
    'StabSel_method'           : Str,
    'StabSel_B'                : Int,
    'StabSel_q'                : Int,
    'StabSel_percent_nS'       : Float,
    'StabSel_lamin'            : Float,
    'StabSel_threshold'        : Float,
    'StabSel_threshold_label'  : Float, # might unneeded here, but needed for visualisation

    #LAMfixed parameters :
    'LAMfixed' : Bool,
    'LAMfixed_numerical_method' : Str,
    'LAMfixed_lam'              : Float, # can be str as well for now !
    'LAMfixed_true_lam'         : Bool
}
regress_parameter_descriptions={
    'y': 'Vector representing the output of the problem',
    #Formulation parameters
    'concomitant': 'True if the formulation of the problem should be with an M_estimation of sigma. Default value = True',
    'huber'      : 'True if the formulation of the problem should be robust Default value = False',
    'rho'        : 'Value of rho for robust problem. Default value = 1.345',
    'rescale'    : 'if True, then the function rescale() will be applied to data when solving the problem',


    #PATH parameters :
    'PATH' : 'True if path should be computed. Default Value = False',
    'PATH_numerical_method' : 'name of the numerical method that is used, it can be : ‘Path-Alg’ (path algorithm) , ‘P-PDS’ (Projected primal-dual splitting method) , ‘PF-PDS’ (Projection-free primal-dual splitting method) or ‘DR’ (Douglas-Rachford-type splitting method) Default value : ‘choose’, which means that the function choose_numerical_method() will choose it accordingly to the formulation',
    'PATH_n_active'         : 'if it is an integer, then the algo stop computing the path when n_active variables are actives. then the solution does not change from this point. Dafault value : False',
    'PATH_lambdas'          : 'list of lambdas for computinf lasso-path for cross validation on lambda. Default value : np.array([10**(-delta * float(i) / nlam) for i in range(0,nlam) ] ) with delta=2. and nlam = 40',
    'PATH_nlam_log'         : ' number of lambdas required, if the list of lambdas is not specified, in order to use a log-ratio list of lambdas',
    'PATH_lamin_log'        : 'minimum of lambdas required, if the list of lambdas is not specified, in order to use a log-ratio list of lambdas',

    #CV parameters :
    'CV' : 'True if Cross Validation should be computed. Default Value = False',
    'CV_numerical_method' : 'name of the numerical method that is used, it can be : ‘Path-Alg’ (path algorithm) , ‘P-PDS’ (Projected primal-dual splitting method) , ‘PF-PDS’ (Projection-free primal-dual splitting method) or ‘DR’ (Douglas-Rachford-type splitting method) Default value : ‘choose’, which means that the function choose_numerical_method() will choose it accordingly to the formulation',
    'CV_seed'             : 'Seed for random values, for an equal seed, the result will be the same. If set to False/None: pseudo-random vectors Default value : None',
    'CV_lambdas'          : 'list of lambdas for computinf lasso-path for cross validation on lambda. Default value : np.linspace(1., 1e-3, 500)',
    'CV_oneSE'            : 'if set to True, the selected lambda if computed with method ‘one-standard-error’ Default value : True',
    'CV_subsets'          : 'number of subset in the cross validation method Dafault value : 5',
    #StabSel parameters :
    'StabSel' : 'True if Stability Selection should be computed. Default Value = True',
    'StabSel_numerical_method' : 'name of the numerical method that is used, it can be : ‘Path-Alg’ (path algorithm) , ‘P-PDS’ (Projected primal-dual splitting method) , ‘PF-PDS’ (Projection-free primal-dual splitting method) or ‘DR’ (Douglas-Rachford-type splitting method) Default value : ‘choose’, which means that the function choose_numerical_method() will choose it accordingly to the formulation',
    'StabSel_seed'             : 'Seed for random values, for an equal seed, the result will be the same. If set to False/None: pseudo-random vectors Default value : None',
    'StabSel_lam'              : '(only used if method = ‘lam’) lam for which the lasso should be computed. Default value : ‘theoretical’ which mean it will be equal to theoretical_lam once it is computed',
    'StabSel_true_lam'         : '(only used if method = ‘lam’) True if the lambda given is the real lambda, False if it lambda/lambdamax which is between 0 and 1. If True and lam = ‘theoretical’ , then it will takes the value n*theoretical_lam. Default value : True',
    'StabSel_method'           : '‘first’, ‘lam’ or ‘max’ depending on the type of stability selection we do. Default value : ‘first’',
    'StabSel_B'                : 'number of subsample considered. Default value : 50',
    'StabSel_q'                : 'number of selected variable per subsample. Default value : 10',
    'StabSel_percent_nS'       : 'size of subsample relatively to the total amount of sample Default value : 0.5',
    'StabSel_lamin'            : 'lamin when computing the lasso-path for method ‘max’ Default value : 1e-2',
    'StabSel_threshold'        : 'threhold for stability selection Default value : 0.7',
    'StabSel_threshold_label'  : 'threshold to know when the label should be plot on the graph. Default value : 0.4', # might unneeded here, but needed for visualisation

    #LAMfixed parameters :
    'LAMfixed' : 'True if solution for a fixed lambda should be computed. Default Value = False',
    'LAMfixed_numerical_method' : 'name of the numerical method that is used, it can be : ‘Path-Alg’ (path algorithm) , ‘P-PDS’ (Projected primal-dual splitting method) , ‘PF-PDS’ (Projection-free primal-dual splitting method) or ‘DR’ (Douglas-Rachford-type splitting method) Default value : ‘choose’, which means that the function choose_numerical_method() will choose it accordingly to the formulation',
    'LAMfixed_lam'              : 'lam for which the lasso should be computed. Default value : ‘theoretical’ which mean it will be equal to theoretical_lam once it is computed', # can be str as well for now !
    'LAMfixed_true_lam'         : 'True if the lambda given is the real lambda, False if it lambda/lambdamax which is between 0 and 1. If True and lam = ‘theoretical’ , then it will takes the value n*theoretical_lam. Default value : True'
}




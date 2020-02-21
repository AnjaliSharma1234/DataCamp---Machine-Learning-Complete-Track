def predict_with_network(input_data):
    # Calculate node 0 in the first hidden layer
    node_0_0_input = (____ * ____).sum()
    node_0_0_output = relu(____)

    # Calculate node 1 in the first hidden layer
    node_0_1_input = ____
    node_0_1_output = ____

    # Put node values into array: hidden_0_outputs
    hidden_0_outputs = np.array([node_0_0_output, node_0_1_output])
    
    # Calculate node 0 in the second hidden layer
    node_1_0_input = ____
    node_1_0_output = ____

    # Calculate node 1 in the second hidden layer
    node_1_1_input = ____
    node_1_1_output = ____

    # Put node values into array: hidden_1_outputs
    hidden_1_outputs = np.array([node_1_0_output, node_1_1_output])

    # Calculate model output: model_output
    model_output = ____
    
    # Return model_output
    return(model_output)

output = predict_with_network(input_data)
print(output)


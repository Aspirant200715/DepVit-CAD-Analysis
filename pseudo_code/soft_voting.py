import numpy as np

def soft_voting(tile_probs):
    """
    Perform soft voting aggregation on patch-level predictions.

    Parameters:
    ----------
    tile_probs : np.ndarray
        Array of shape (num_tiles, num_classes)
        Each row contains softmax probabilities for a tile.

    Returns:
    -------
    int
        Final predicted class index.
    """
    # Average probabilities across all tiles
    avg_prob = np.mean(tile_probs, axis=0)

    # Return class with highest average probability
    return int(np.argmax(avg_prob))


def soft_voting_with_probs(tile_probs):
    """
    Returns both predicted class and aggregated probabilities.

    Parameters:
    ----------
    tile_probs : np.ndarray
        Array of shape (num_tiles, num_classes)

    Returns:
    -------
    tuple
        (predicted_class, aggregated_probabilities)
    """
    avg_prob = np.mean(tile_probs, axis=0)
    predicted_class = int(np.argmax(avg_prob))

    return predicted_class, avg_prob


if __name__ == "__main__":
    # Example usage

    # Simulated tile predictions (3 tiles, 3 classes)
    tile_probs = np.array([
        [0.7, 0.2, 0.1],
        [0.6, 0.3, 0.1],
        [0.2, 0.7, 0.1]
    ])

    pred_class, probs = soft_voting_with_probs(tile_probs)

    print("Aggregated probabilities:", probs)
    print("Final predicted class:", pred_class)
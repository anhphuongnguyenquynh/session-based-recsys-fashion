**Session-based Recommendation System in Fashion**

This repository contains my exploration and implementation for a Session-based Recommendation System challenge, focusing on predicting the next item a user will interact with during an ongoing session.

## Overview
Different from traditional recommendation system that contains user purchase histories and demographic, session-based recommendation system is a short-term user interactions from anonymous users. These sequences of interactions may be clicks, views or purchases with items. The challenge is inspired by [RecsysACM Challenge in 2022](https://www.recsyschallenge.com/2022/).

## Solutions

1. Preprocessing
- Sequence generation: generate a item sequence interaction and padding with the same length.
- Apply aata augmentation techniques to improve robustness and alleviate sparsity with:
 + Noise Injection: randomly choose an item (negative sample) not included in the original item sequence. Inject the negative sample into a random position in the sequence.
 + Redundancy Injection: Randomly choose an item (positive sample) from the original item sequence. Inject the positive sample into a random position in the sequence.
 + Random Swap: Random chooses two items in the sentences and swap in their positions.
 + Random Deletion: Randomly remove each items in the sequences with probability p. In this project, instead of remove probability p items, just remove one item in the session.
 + Synonym Replacement: Randomly choose n items from the sequence. Replace each of these items with one of its similar item chosan at random.

2. Processing
Reimplement three popular deep learning methods:
 + 2.1 Neural Attentive Recommendation System (NARM)
 + 2.2 Transformer-based Recommendation System (inspired by Behaviour Sequence Transformer Model - BST)
 + 2.3 Bidirectional Encoder Representations from Transformers - BERT4Rec
 
## Results





  

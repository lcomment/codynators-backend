import pickle 

# goal is to "pickle" (save to a file) the header and interview tree so that file can be used
# later to create Python objects from the file to be used in another Python program
# by "unpickling" (loading the saved file) back into a Python object in that other Python program

header = ["level", "lang", "tweets", "phd"]
interview_tree = \
["Attribute", "level", 
    ["Value", "Senior", 
        ["Attribute", "tweets", 
            ["Value", "yes", 
                ["Leaf", "True", 2, 5]
            ],
            ["Value", "no", 
                ["Leaf", "False", 3, 5]
            ]
        ]
    ],
    ["Value", "Mid", 
        ["Leaf", "True", 4, 14]
    ],
    ["Value", "Junior", 
        ["Attribute", "phd", 
            ["Value", "yes", 
                ["Leaf", "False", 2, 5]
            ],
            ["Value", "no", 
                ["Leaf", "True", 3, 5]
            ]
        ]
    ]
]

packaged_object = [header, interview_tree]
# pickle packaged_object to a file tree.p
outfile = open("tree.p", "wb")
pickle.dump(packaged_object, outfile)
outfile.close()
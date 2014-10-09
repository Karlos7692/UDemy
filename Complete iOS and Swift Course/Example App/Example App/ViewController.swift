//
//  ViewController.swift
//  Example App
//
//  Created by Karl Christopher Nelson on 7/10/2014.
//  Copyright (c) 2014 Karl Nelson. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var myLabel: UILabel!
        
    @IBAction func buttonTapped() {
        myLabel.text = "It Worked!";
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        println("Hello World!")
        
    }

   

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}


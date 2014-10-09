//
//  ViewController.swift
//  CatYears
//
//  Created by Karl Christopher Nelson on 8/10/2014.
//  Copyright (c) 2014 Karl Nelson. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var answerLabel: UILabel!
    
    @IBOutlet weak var answerField: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    @IBAction func answerButtonTapped() {
        var textString = answerField.text
        var answer = "Please put the number of human years above."
        if ((textString) != "") {
            var catYears = textString.toInt()! *  7
            answer = "Your cat is \(catYears) old."
        }
        
        answerLabel.text = answer;
        
    }
    
    func doneWithNumberPad(){
        println("Selector Called")
        answerField.resignFirstResponder()
    }

}


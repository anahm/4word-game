//
//  HelloWorldViewController.h
//  HelloWorld
//
//  Created by Ali Nahm on 5/31/13.
//  Copyright (c) 2013 Ali Nahm. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface HelloWorldViewController : UIViewController <UITextFieldDelegate>
- (IBAction)changeGreeting:(id)sender;
@property (weak, nonatomic) IBOutlet UITextField *textfield;
@property (weak, nonatomic) IBOutlet UILabel *label;

@property (copy, nonatomic) NSString *userName;

@end
